#!/usr/bin/python
# Classification (U)

"""Program:  mysql_db_admin.py

    Description:  A MySQL Database Administration program that can run a number
        of different administration functions such as compacting/defraging a
        table, checking a table for errors, analyze a table's key distribution
        (index check), or get a checksum on a table.  The options will allow
        for for a single object, multiple objects, or all objects.  Also can
        return the database's status to include uptime, connection usage,
        memory use, and database server status.

    Usage:
        mysql_db_admin.py -c file -d path {-C [db_name [db_name ...]]
            | -A [db_name [db_name ...] | -S [db_name [db_name ...]]
            | -D [db_name [db_name ...] ] | -M {-j
            | -i {db_name: table_name} | -m file} | -o dir_path/file}}
            [ -t [table_name [table_name ...]]] [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -C [database name(s)] => Check a table for errors.
        -A [database name(s)] => Analyze a table's key distribution
            (checks the table's indexes).
        -S [database name(s)] => Return a checksum on a table.
        -D [database name(s)] => Optimize/defragment a table (command
            runs an Alter Table and Analyze command on the table).
        -M Display the current database status, such as uptime, memory
            use, connection usage, and status.
        -m file => Mongo config file.  Is loaded as a python, do not
            include the .py extension with the name.
        -j => Convert output to JSON format.
        -i { database:collection } => Name of database and collection.
            Delimited by colon (:).  Default: sysmon:mysql_db_status
        -o path/file => Directory path and file name for output.
        -t [ table name(s) ] =>  Used with the -C, -A, -S & -D options.
        -v => Display version of this program.
        -h => Help and usage message.

         NOTE 1:  -v or -h overrides the other options.

        NOTE 2:  Options -A, -C, -D, and -S: If no name is passed, will
             do all database names, can also pass multiple databases
            names to the option, must be space delimited.

        NOTE 3:  Option -t: If not name is passed, will
            do all table names, can also pass multiple table names to
            the option, must be space delimited.  If no -t option is
            used, will do all tables in the database.

        NOTE 4:  Default output is in standard output, unless -j option
            is selected.

    Notes:
        Database configuration file format (mysql_{host}.py):
            # Configuration file for {Database Name/Server}
            user = "root"
            passwd = "ROOT_PASSWORD"
            # DO NOT USE 127.0.0.1 for the master/source, use actual IP.
            host = "IP_ADDRESS"
            serv_os = "Linux" or "Solaris"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 3306)
            cfg_file = "DIRECTORY_PATH/my.cnf"
            sid = "SERVER_ID"
            extra_def_file = "DIRECTORY_PATH/myextra.cfg"

        NOTE:  Include the cfg_file even if running remotely as the file will
            be used in future releases.

        configuration modules -> name is runtime dependent as it can be
            used to connect to different databases with different names.

        Defaults Extra File format (filename.cfg):
            [client]
            password="ROOT_PASSWORD"
            socket="DIRECTORY_PATH/mysql.sock"

        NOTE:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.

    Example:
        mysql_db_admin.py -c mysql -d config -D test -t users

"""

# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function
import sys
import datetime

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.cmds_gen as cmds_gen
import mysql_lib.mysql_libs as mysql_libs
import mysql_lib.mysql_class as mysql_class
import mongo_lib.mongo_libs as mongo_libs
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def run_analyze(server, db, tbl, **kwargs):

    """Function:  run_analyze

    Description:  Calls the analyze table command and prints the results.

    Arguments:
        (input) server -> Server instance.
        (input) db -> Database name.
        (input) tbl -> Table name.
        (input) **kwargs:
            sys_dbs -> List of system databases to skip.

    """

    if db not in kwargs.get("sys_dbs", []):

        for x in mysql_libs.analyze_tbl(server, db, tbl):
            print("DB: {0:20} Table: {1:50}\t".format(db, tbl), end="")
            gen_libs.prt_msg(x["Msg_type"], x["Msg_text"])


def run_checksum(server, db, tbl, **kwargs):

    """Function:  run_checksum

    Description:  Calls the checksum table command and prints the results.

    Arguments:
        (input) server -> Server instance.
        (input) db -> Database name.
        (input) tbl -> Table name.

    """

    for x in mysql_libs.checksum(server, db, tbl):
        print("DB: {0:20} Table: {1:50}\tCheckSum: {2}".format(db, tbl,
                                                               x["Checksum"]))


def run_optimize(server, db, tbl, **kwargs):

    """Function:  run_optimize

    Description:  Calls the optimize table command and print the results.

    Arguments:
        (input) server -> Server database instance.
        (input) db -> Database name.
        (input) tbl -> Table name.
        (input) **kwargs:
            sys_dbs -> List of system databases to skip.

    """

    if db not in kwargs.get("sys_dbs", []):

        for x in mysql_libs.optimize_tbl(server, db, tbl):
            if x["Msg_type"] == "note" and x["Msg_text"] == \
               "Table does not support optimize, doing recreate + \
analyze instead":

                pass

            else:
                print("DB: {0:20} Table: {1:50}\t".format(db, tbl), end="")
                gen_libs.prt_msg(x["Msg_type"], x["Msg_text"])


def run_check(server, db, tbl, **kwargs):

    """Function:  run_check

    Description:  Calls the check table command and print the results.

    Arguments:
        (input) server -> Server database instance.
        (input) db -> Database name.
        (input) tbl -> Table name.

    """

    for x in mysql_libs.check_tbl(server, db, tbl):
        print("DB: {0:20} Table: {1:50}\t".format(db, tbl), end="")
        gen_libs.prt_msg(x["Msg_type"], x["Msg_text"])


def detect_dbs(sub_db_list, full_db_list, **kwargs):

    """Function:  detect_dbs

    Description:  Finds which databases in Database list 1 are not present in
        Database list 2.

    Arguments:
        (input) sub_db_list -> Subset Database list.
        (input) full_db_list -> Full Database list.

    """

    dbs = list(set(sub_db_list) - set(full_db_list))

    if dbs:
        print("Warning: Database(s) that do not exist: %s." % (dbs))


def process_request(server, func_name, db_name=None, tbl_name=None, **kwargs):

    """Function:  process_request

    Description:  Prepares for the type of check based on the arguments passed
        to the function and then calls the "func_name" function.
        NOTE:  If db_name and/or tbl_name is set to None, then assumes to
            process all databases/tables repsectively.

    Arguments:
        (input) server -> Database server instance.
        (input) func_name -> Name of a function.
        (input) db_name -> Database name.
        (input) tbl_name -> Table name.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    if db_name is None:
        db_name = []

    if tbl_name is None:
        tbl_name = []

    db_list = gen_libs.dict_2_list(mysql_libs.fetch_db_dict(server),
                                   "Database")

    # Process all tables in all databases.
    if not db_name:

        for db in db_list:

            for tbl in gen_libs.dict_2_list(mysql_libs.fetch_tbl_dict(server,
                                                                      db),
                                            "table_name"):

                func_name(server, db, tbl, **kwargs)

    # Process all tables in listed databases.
    elif not tbl_name:

        detect_dbs(db_name, db_list, **kwargs)

        for db in set(db_name) & set(db_list):

            for tbl in gen_libs.dict_2_list(mysql_libs.fetch_tbl_dict(server,
                                                                      db),
                                            "table_name"):

                func_name(server, db, tbl, **kwargs)

    # Process listed tables in listed databases.
    else:

        detect_dbs(db_name, db_list, **kwargs)

        for db in set(db_name) & set(db_list):
            tbl_list = gen_libs.dict_2_list(mysql_libs.fetch_tbl_dict(server,
                                                                      db),
                                            "table_name")

            tbls = list(set(tbl_name) - set(tbl_list))

            if tbls:
                print("Warning: Database (%s) Tables that do not exist %s."
                      % (db, tbls))

            for tbl in set(tbl_name) & set(tbl_list):
                func_name(server, db, tbl, **kwargs)


def analyze(server, args_array, **kwargs):

    """Function:  analyze

    Description:  Sets up the processing for the analyze table command.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            sys_dbs -> List of system databases to skip.
            multi_val -> List of options that may have multiple values.

    """

    process_request(server, run_analyze, args_array["-A"],
                    args_array.get("-t", None), **kwargs)


def checksum(server, args_array, **kwargs):

    """Function:  checksum

    Description:  Sets up the processing for the checksum table command.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            multi_val -> List of options that may have multiple values.

    """

    process_request(server, run_checksum, args_array["-S"],
                    args_array.get("-t", None), **kwargs)


def optimize(server, args_array, **kwargs):

    """Function:  optimize

    Description:  Sets up the processing for the optimization table command.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    process_request(server, run_optimize, args_array["-D"],
                    args_array.get("-t", None), **kwargs)


def check(server, args_array, **kwargs):

    """Function:  check

    Description:  Sets up the processing for the check table command.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            multi_val -> List of options that may have multiple values.

    """

    process_request(server, run_check, args_array["-C"],
                    args_array.get("-t", None), **kwargs)


def status(server, args_array, **kwargs):

    """Function:  status

    Description:  Retrieves a number of database status variables and sends
        them out either in standard out (print) or to a JSON format which
        is printed and poissibly inserted into a Mongo database.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            ofile -> file name - Name of output file.
            db_tbl database:table_name -> Mongo database and table name.
            class_cfg -> Mongo server configuration.

    """

    server.upd_srv_stat()

    if "-j" in args_array:
        outdata = {"Application": "MySQL Database",
                   "Server": server.name,
                   "Asof": datetime.datetime.strftime(datetime.datetime.now(),
                                                      "%Y-%m-%d %H:%M:%S")}

    else:
        print("\nDatabase Status Check for Server: %s" % (server.name))

    if "-j" in args_array:
        outdata.update({"Memory": {"Current_Usage": server.cur_mem_mb,
                                   "Max_Usage": server.max_mem_mb,
                                   "Percent_Used": server.prct_mem},
                        "Uptime": server.days_up,
                        "Connections": {"Current_Connected": server.cur_conn,
                                        "Max_Connections": server.max_conn,
                                        "Percent_Used": server.prct_conn}})

    else:
        gen_libs.prt_msg("Uptime (days)", server.days_up, 0)
        gen_libs.prt_msg("Memory", "", 0)
        gen_libs.prt_msg("Max Mem", server.max_mem_mb, 1)
        gen_libs.prt_msg("Current Mem", server.cur_mem_mb, 1)
        gen_libs.prt_msg("Percent Used", server.prct_mem, 1)
        gen_libs.prt_msg("Connections", "", 0)
        gen_libs.prt_msg("Max Connections", server.max_conn, 1)
        gen_libs.prt_msg("Current Connections", server.cur_conn, 1)
        gen_libs.prt_msg("Percent Used", server.prct_conn, 1)

    if "-j" in args_array:
        mongo_libs.json_prt_ins_2_db(outdata, **kwargs)


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    server = mysql_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mysql_class.Server)
    server.connect()

    outfile = args_array.get("-o", None)
    db_tbl = args_array.get("-i", None)

    mongo = None
    if args_array.get("-m", None):
        mongo = gen_libs.load_module(args_array["-m"], args_array["-d"])

    # Intersect args_array and func_dict to determine which functions to call.
    for x in set(args_array.keys()) & set(func_dict.keys()):
        func_dict[x](server, args_array, ofile=outfile, db_tbl=db_tbl,
                     class_cfg=mongo, **kwargs)

    cmds_gen.disconnect([server])


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_con_req_list -> contains the options that require other options.
        opt_def_dict -> contains options with their default values.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        opt_xor_dict -> contains options which are XOR with its values.
        sys_dbs -> contains a list of system databases that will be skipped
            over for some functions.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-A": analyze, "-C": check, "-D": optimize, "-S": checksum,
                 "-M": status}
    opt_con_req_list = {"-i": ["-m"]}
    opt_def_dict = {"-t": None, "-A": [], "-C": [], "-D": [], "-S": [],
                    "-i": "sysmon:mysql_db_status"}
    opt_multi_list = ["-A", "-C", "-D", "-S", "-t"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-t", "-A", "-C", "-D", "-S", "-i", "-m", "-o"]
    opt_xor_dict = {"-A": ["-C", "-D", "-M", "-S"],
                    "-C": ["-A", "-D", "-M", "-S"],
                    "-D": ["-A", "-C", "-M", "-S"],
                    "-S": ["-A", "-C", "-D", "-M"],
                    "-M": ["-A", "-C", "-D", "-S"]}
    sys_dbs = ["performance_schema", "information_schema", "mysql"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list, opt_def_dict,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list):
        run_program(args_array, func_dict, sys_dbs=sys_dbs,
                    multi_val=opt_multi_list)


if __name__ == "__main__":
    sys.exit(main())
