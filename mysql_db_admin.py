#!/usr/bin/python
# Classification (U)

"""Program:  mysql_db_admin.py

    Description:  Run a number of different administration functions such as
        compacting/defraging a table, checking a table for errors, analyze a
        table's key distribution (index check), or get a checksum on a table.
        The options will allow for for a single object, multiple objects, or
        all objects.  Also can return the database's status to include uptime,
        connection usage, memory use, and database server status.

    Usage:
        mysql_db_admin.py -c mysql_cfg -d path
            {-C [db_name [db_name2 ...]] [-t table_name [table_name2 ...]] |
             -A [db_name [db_name2 ...] [-t table_name [table_name2 ...]] |
             -S [db_name [db_name2 ...]] [-t table_name [table_name2 ...]] |
             -D [db_name [db_name2 ...]] [-t table_name [table_name2 ...]] |
             -M [-j [-f]] | [-i [db_name:table_name] -m config_file] |
                [-e to_email [to_email2 ...] [-s subject_line] [-u]] | [-z] |
                [-o dir_path/file [-a]] |
             -L [-a]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c mysql_cfg => MySQL configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.

        -C [database name(s)] => Check a table for errors.
            -t table name(s) => Table names to check.

        -A [database name(s)] => Analyze a table's key distribution, checks the
                table's indexes.
            -t table name(s) => Table names to check.

        -S [database name(s)] => Return a checksum on a table.
            -t table name(s) => Table names to check.

        -D [database name(s)] => Optimize/defragment a table, the command
                runs an Alter Table and Analyze command on the table.
            -t table name(s) => Table names to check.

        -M => Display the current database status, such as uptime, memory
                use, connection usage, and status.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
            -j => Convert output to JSON format.
                -f => Flatten the JSON data structure to file and standard out.
            -i {database:collection} => Name of database and collection.
                Default: sysmon:mysql_db_status
            -o path/file => Directory path and file name for output.
                -a => Append output to output file.
            -s subject_line => Subject line of email.  Optional, will create
                own subject line if one is not provided.
            -e to_email_address(es) => Enables emailing capability for an
                    option if the option allows it.  Sends output to one or
                    more email addresses.  Email addresses are delimited by
                    spaces.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.

        -L => Display list of user databases.
            -k => Include system databases in the list.

        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  Options -A, -C, -D, and -S: If no name is passed, will
             do all database names, can also pass multiple databases
            names to the option, must be space delimited.
        NOTE 3:  Option -t: If no name is passed, will do all table names, can
            also pass multiple table names to the option, must be space
            delimited.  If no -t option is used, will do all tables in the
            database.
        NOTE 4:  Default output is in standard output, unless -j option
            is selected.

    Notes:
        Database configuration file format (config/mysql_cfg.py.TEMPLATE):
        WARNING:  Do not use the loopback IP or 'localhost' for the "host"
        variable, use the actual IP.

            # Configuration file for MySQL database server.
            user = "USER"
            japd = "PSWORD"
            host = "HOST_IP"
            name = "HOST_NAME"
            sid = SERVER_ID
            extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
            serv_os = "Linux"
            port = 3306
            cfg_file = "MYSQL_DIRECTORY/mysqld.cnf"

            # If SSL connections are being used, configure one or more of these
                entries:
            ssl_client_ca = None
            ssl_client_key = None
            ssl_client_cert = None

            # Only changes these if necessary and have knowledge in MySQL
                SSL configuration setup:
            ssl_client_flag = None
            ssl_disabled = False
            ssl_verify_id = False
            ssl_verify_cert = False

            # TLS versions: Set the TLS versions allowed in the connection
            tls_versions = []

        NOTE 1:  Include the cfg_file even if running remotely as the file will
            be used in future releases.
        NOTE 2:  In MySQL 5.6 - it now gives warning if password is passed on
            the command line.  To suppress this warning, will require the use
            of the --defaults-extra-file option (i.e. extra_def_file) in the
            database configuration file.  See below for the
            defaults-extra-file format.
        NOTE 3:  Ignore the rep_user and rep_japd entries.  Not required.

        Defaults Extra File format (config/mysql.cfg.TEMPLATE)
            password="PSWORD"
            socket=DIRECTORY_PATH/mysqld.sock

        NOTE 1:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.
        NOTE 2:  The --defaults-extra-file option will be overridden if there
            is a ~/.my.cnf or ~/.mylogin.cnf file located in the home directory
            of the user running this program.  The extras file will in effect
            be ignored.
        NOTE 3:  Socket use is only required to be set in certain conditions
            when connecting using localhost.

        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format for the Mongo connection used for
            inserting data into a database.
            There are two ways to connect:  single or replica set.

            Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            host = "HOST_IP"
            name = "HOSTNAME"
            port = 27017
            conf_file = None
            auth = True
            auth_db = "admin"
            auth_mech = "SCRAM-SHA-1"

            Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

            Note:  If using SSL connections then set one or more of the
                following entries.  This will automatically enable SSL
                connections. Below are the configuration settings for SSL
                connections.  See configuration file for details on each entry:

            ssl_client_ca = None
            ssl_client_key = None
            ssl_client_cert = None
            ssl_client_phrase = None

            Note:  FIPS Environment for Mongo.
              If operating in a FIPS 104-2 environment, this package will
              require at least a minimum of pymongo==3.8.0 or better.  It will
              also require a manual change to the auth.py module in the pymongo
              package.  See below for changes to auth.py.

            - Locate the auth.py file python installed packages on the system
                in the pymongo package directory.
            - Edit the file and locate the "_password_digest" function.
            - In the "_password_digest" function there is an line that should
                match: "md5hash = hashlib.md5()".  Change it to
                "md5hash = hashlib.md5(usedforsecurity=False)".
            - Lastly, it will require the Mongo configuration file entry
                auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.

        Configuration modules -> name is runtime dependent as it can be
            used to connect to different databases with different names.

    Example:
        mysql_db_admin.py -c mysql -d config -D test -t users

"""

# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function
import sys
import datetime

# Third party
import json

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import mysql_lib.mysql_libs as mysql_libs
import mysql_lib.mysql_class as mysql_class
import mongo_lib.mongo_libs as mongo_libs
import version

__version__ = version.__version__

# Global
PRT_TEMPLATE = "DB: {0:20} Table: {1:50}\t"


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def run_analyze(server, dbs, tbl, **kwargs):

    """Function:  run_analyze

    Description:  Calls the analyze table command and prints the results.

    Arguments:
        (input) server -> Server instance.
        (input) dbs -> Database name.
        (input) tbl -> Table name.
        (input) **kwargs:
            sys_dbs -> List of system databases to skip.

    """

    global PRT_TEMPLATE

    if dbs not in list(kwargs.get("sys_dbs", [])):

        for item in mysql_libs.analyze_tbl(server, dbs, tbl):
            print(PRT_TEMPLATE.format(dbs, tbl), end="")
            gen_libs.prt_msg(item["Msg_type"], item["Msg_text"])


def run_checksum(server, dbs, tbl, **kwargs):

    """Function:  run_checksum

    Description:  Calls the checksum table command and prints the results.

    Arguments:
        (input) server -> Server instance.
        (input) dbs -> Database name.
        (input) tbl -> Table name.

    """

    for item in mysql_libs.checksum(server, dbs, tbl):
        print("DB: {0:20} Table: {1:35}  CheckSum:\t{2}".format(
            dbs, tbl, item["Checksum"]))


def run_optimize(server, dbs, tbl, **kwargs):

    """Function:  run_optimize

    Description:  Calls the optimize table command and print the results.

    Arguments:
        (input) server -> Server instance.
        (input) dbs -> Database name.
        (input) tbl -> Table name.
        (input) **kwargs:
            sys_dbs -> List of system databases to skip.

    """

    global PRT_TEMPLATE

    if dbs not in list(kwargs.get("sys_dbs", [])):

        for item in mysql_libs.optimize_tbl(server, dbs, tbl):
            if item["Msg_type"] == "note" and item["Msg_text"] == \
               "Table does not support optimize, doing recreate + \
analyze instead":

                continue

            else:
                print(PRT_TEMPLATE.format(dbs, tbl), end="")
                gen_libs.prt_msg(item["Msg_type"], item["Msg_text"])


def run_check(server, dbs, tbl, **kwargs):

    """Function:  run_check

    Description:  Calls the check table command and print the results.

    Arguments:
        (input) server -> Server instance.
        (input) dbs -> Database name.
        (input) tbl -> Table name.

    """

    global PRT_TEMPLATE

    for item in mysql_libs.check_tbl(server, dbs, tbl):
        print(PRT_TEMPLATE.format(dbs, tbl), end="")
        gen_libs.prt_msg(item["Msg_type"], item["Msg_text"])


def detect_dbs(sub_db_list, full_db_list, **kwargs):

    """Function:  detect_dbs

    Description:  Finds which databases in Database list 1 are not present in
        Database list 2.

    Arguments:
        (input) sub_db_list -> Subset Database list.
        (input) full_db_list -> Full Database list.

    """

    sub_db_list = list(sub_db_list)
    full_db_list = list(full_db_list)
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
        (input) server -> Server instance.
        (input) func_name -> Name of a function.
        (input) db_name -> Database name.
        (input) tbl_name -> Table name.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    db_name = list() if db_name is None else list(db_name)
    tbl_name = list() if tbl_name is None else list(tbl_name)
    db_list = gen_libs.dict_2_list(mysql_libs.fetch_db_dict(server),
                                   "Database")
    dict_key = "table_name"

    # Determine the MySQL version for dictionary key name
    if mysql_class.fetch_sys_var(server, "version",
                                 level="session")["version"] >= "8.0":
        dict_key = "TABLE_NAME"

    # Process all databases
    if not db_name:
        _proc_all_dbs(server, func_name, db_list, dict_key, **kwargs)

    # Process all tables in some databases
    elif not tbl_name:
        _proc_all_tbls(server, func_name, db_list, db_name, dict_key, **kwargs)

    # Process specific tables.
    else:
        _proc_some_tbls(server, func_name, db_list, db_name, tbl_name,
                        dict_key, **kwargs)


def _proc_all_dbs(server, func_name, db_list, dict_key, **kwargs):

    """Function:  _proc_all_dbs

    Description:  Private function for process_requests().  Process all
        databases.

    Arguments:
        (input) server -> Server instance.
        (input) func_name -> Name of a function.
        (input) db_list -> List of all databases.
        (input) dict_key -> Dictionary key for fetch_tbl_dict call.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    for dbs in db_list:
        for tbl in gen_libs.dict_2_list(mysql_libs.fetch_tbl_dict(server, dbs),
                                        dict_key):
            func_name(server, dbs, tbl, **kwargs)


def _proc_all_tbls(server, func_name, db_list, db_name, dict_key, **kwargs):

    """Function:  _proc_all_tbls

    Description:  Private function for process_requests().  Process all tables
        in listed databases.

    Arguments:
        (input) server -> Server instance.
        (input) func_name -> Name of a function.
        (input) db_list -> List of all databases.
        (input) db_name -> List of database names.
        (input) dict_key -> Dictionary key for fetch_tbl_dict call.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    db_name = list(db_name)
    db_list = list(db_list)
    detect_dbs(db_name, db_list, **kwargs)

    for dbs in set(db_name) & set(db_list):
        for tbl in gen_libs.dict_2_list(mysql_libs.fetch_tbl_dict(server, dbs),
                                        dict_key):
            func_name(server, dbs, tbl, **kwargs)


def _proc_some_tbls(server, func_name, db_list, db_name, tbl_name, dict_key,
                    **kwargs):

    """Function:  _proc_some_tbls

    Description:  Private function for process_requests().  Process somes
        tables in listed databases.

    Arguments:
        (input) server -> Server instance.
        (input) func_name -> Name of a function.
        (input) db_list -> List of all databases.
        (input) db_name -> List of database names.
        (input) tbl_name -> List of table names.
        (input) dict_key -> Dictionary key for fetch_tbl_dict call.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    db_name = list(db_name)
    db_list = list(db_list)
    tbl_name = list(tbl_name)
    detect_dbs(db_name, db_list, **kwargs)

    for dbs in set(db_name) & set(db_list):
        tbl_list = gen_libs.dict_2_list(mysql_libs.fetch_tbl_dict(server, dbs),
                                        dict_key)
        tbls = list(set(tbl_name) - set(tbl_list))

        if tbls:
            print("Warning: Database (%s) Tables that do not exist %s."
                  % (dbs, tbls))

        for tbl in set(tbl_name) & set(tbl_list):
            func_name(server, dbs, tbl, **kwargs)


def analyze(server, args_array, **kwargs):

    """Function:  analyze

    Description:  Sets up the processing for the analyze table command.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of command line options.
        (input) **kwargs:
            sys_dbs -> List of system databases to skip.
            multi_val -> List of options that may have multiple values.

    """

    args_array = dict(args_array)
    process_request(server, run_analyze, args_array["-A"],
                    args_array.get("-t", None), **kwargs)


def checksum(server, args_array, **kwargs):

    """Function:  checksum

    Description:  Sets up the processing for the checksum table command.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of command line options.
        (input) **kwargs:
            multi_val -> List of options that may have multiple values.

    """

    args_array = dict(args_array)
    process_request(server, run_checksum, args_array["-S"],
                    args_array.get("-t", None), **kwargs)


def optimize(server, args_array, **kwargs):

    """Function:  optimize

    Description:  Sets up the processing for the optimization table command.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of command line options.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    args_array = dict(args_array)
    process_request(server, run_optimize, args_array["-D"],
                    args_array.get("-t", None), **kwargs)


def check(server, args_array, **kwargs):

    """Function:  check

    Description:  Sets up the processing for the check table command.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of command line options.
        (input) **kwargs:
            multi_val -> List of options that may have multiple values.

    """

    args_array = dict(args_array)
    process_request(server, run_check, args_array["-C"],
                    args_array.get("-t", None), **kwargs)


def status(server, args_array, **kwargs):

    """Function:  status

    Description:  Retrieves a number of database status variables and sends
        them out either in standard out (print) or to a JSON format which
        is printed and poissibly inserted into a Mongo database.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of command line options.
        (input) **kwargs:
            ofile -> file name - Name of output file.
            db_tbl database:table_name -> Mongo database and table name.
            class_cfg -> Mongo server configuration.
            mail -> Mail instance.

    """

    args_array = dict(args_array)
    server.upd_srv_stat()

    mode = "a" if args_array.get("-a", False) else "w"

    outdata = {"Application": "MySQL Database",
               "Server": server.name,
               "AsOf": datetime.datetime.strftime(datetime.datetime.now(),
                                                  "%Y-%m-%d %H:%M:%S"),
               "Memory": {"CurrentUsage": server.cur_mem_mb,
                          "MaxUsage": server.max_mem_mb,
                          "PercentUsed": server.prct_mem},
               "UpTime": server.days_up,
               "Connections": {"CurrentConnected": server.cur_conn,
                               "MaxConnections": server.max_conn,
                               "PercentUsed": server.prct_conn}}

    if "-j" in args_array:
        _process_json(args_array, outdata, mode, **kwargs)

    else:
        _process_non_json(server, args_array, outdata, mode, **kwargs)


def _process_json(args_array, outdata, mode, **kwargs):

    """Function:  _process_json

    Description:  Private function for status to process json format data.

    Arguments:
        (input) args_array -> Dictionary of command line options.
        (input) outdata -> Dictionary of performance data.
        (input) mode -> File write mode.
        (input) **kwargs:
            ofile -> file name - Name of output file.
            db_tbl database:table_name -> Mongo database and table name.
            class_cfg -> Mongo server configuration.
            mail -> Mail instance.

    """

    indent = None if args_array.get("-f", False) else 4

    jdata = json.dumps(outdata, indent=indent)
    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)
    ofile = kwargs.get("ofile", None)
    mail = kwargs.get("mail", None)

    if mongo_cfg and db_tbl:
        dbs, tbl = db_tbl.split(":")
        conn_stats = mongo_libs.ins_doc(mongo_cfg, dbs, tbl, outdata)

        if not conn_stats[0]:
            print("Error: status.mongo_insert: %s" % (conn_stats[1]))

    if ofile:
        gen_libs.write_file(ofile, mode, jdata)

    if mail:
        mail.add_2_msg(jdata)
        mail.send_mail(use_mailx=args_array.get("-u", False))

    if not args_array.get("-z", False):
        gen_libs.print_data(jdata)


def _process_non_json(server, args_array, outdata, mode, **kwargs):

    """Function:  _process_non_json

    Description:  Private function for status to process non-json format
        data.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of command line options.
        (input) outdata -> Dictionary of performance data.
        (input) mode -> File write mode.
        (input) **kwargs:
            ofile -> file name - Name of output file.
            mail -> Mail instance.

    """

    args_array = dict(args_array)
    outdata = dict(outdata)
    ofile = kwargs.get("ofile", None)
    mail = kwargs.get("mail", None)
    pdata = ""

    for key, value in outdata.items():
        pdata += "{}: {}".format(key, value) + "\n"

    if not args_array.get("-z", False):
        print("\nDatabase Status Check for Server: %s" % (server.name))
        gen_libs.prt_msg("Uptime (days)", server.days_up, 0)
        gen_libs.prt_msg("Memory", "", 0)
        gen_libs.prt_msg("Max Mem", server.max_mem_mb, 1)
        gen_libs.prt_msg("Current Mem", server.cur_mem_mb, 1)
        gen_libs.prt_msg("Percent Used", server.prct_mem, 1)
        gen_libs.prt_msg("Connections", "", 0)
        gen_libs.prt_msg("Max Connections", server.max_conn, 1)
        gen_libs.prt_msg("Current Connections", server.cur_conn, 1)
        gen_libs.prt_msg("Percent Used", server.prct_conn, 1)

    if ofile:
        gen_libs.write_file(ofile, mode, pdata)

    if mail:
        mail.add_2_msg(pdata)
        mail.send_mail(use_mailx=args_array.get("-u", False))


def listdbs(server, args_array, **kwargs):

    """Function:  listdbs

    Description:  List user or user/system databases in the database instance.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of command line options.
        (input) **kwargs:
            sys_dbs -> List of system databases.

    """

    args_array = dict(args_array)
    sys_dbs = list(kwargs.get("sys_dbs", []))
    db_list = gen_libs.dict_2_list(mysql_libs.fetch_db_dict(server),
                                   "Database")

    if "-k" in args_array:
        print("List of user and system databases:")

        for item in db_list:
            print("    %s" % (item))

    else:
        print("List of user databases:")

        for item in gen_libs.del_not_and_list(db_list, sys_dbs):
            print("    %s" % (item))


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dictionary of command line options.
        (input) func_dict -> Dictionary of functions.
        (input) **kwargs:
            sys_dbs -> List of system databases.
            multi_val -> List of options that may have multiple values.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    server = mysql_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mysql_class.Server)
    server.connect(silent=True)

    if server.conn_msg:
        print("run_program:  Error encountered on server(%s):  %s" %
              (server.name, server.conn_msg))

    else:
        outfile = args_array.get("-o", None)
        db_tbl = args_array.get("-i", None)
        mongo = None
        mail = None

        if args_array.get("-m", None):
            mongo = gen_libs.load_module(args_array["-m"], args_array["-d"])

        if args_array.get("-e", None):
            mail = gen_class.setup_mail(args_array.get("-e"),
                                        subj=args_array.get("-s", None))

        # Intersect args_array & func_dict to determine which functions to call
        for item in set(args_array.keys()) & set(func_dict.keys()):
            func_dict[item](server, args_array, ofile=outfile, db_tbl=db_tbl,
                            class_cfg=mongo, mail=mail, **kwargs)

        mysql_libs.disconnect(server)


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

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-A": analyze, "-C": check, "-D": optimize, "-S": checksum,
                 "-M": status, "-L": listdbs}
    opt_con_req_list = {"-i": ["-m"], "-s": ["-e"], "-u": ["-e"]}
    opt_def_dict = {"-t": None, "-A": [], "-C": [], "-D": [], "-S": [],
                    "-i": "sysmon:mysql_db_status"}
    opt_multi_list = ["-A", "-C", "-D", "-S", "-t", "-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-t", "-A", "-C", "-D", "-S", "-i", "-m", "-o",
                    "-e", "-s", "-y"]
    opt_xor_dict = {"-A": ["-C", "-D", "-M", "-S", "-L"],
                    "-C": ["-A", "-D", "-M", "-S", "-L"],
                    "-D": ["-A", "-C", "-M", "-S", "-L"],
                    "-S": ["-A", "-C", "-D", "-M", "-L"],
                    "-M": ["-A", "-C", "-D", "-S", "-L"],
                    "-L": ["-A", "-C", "-D", "-S", "-M"]}
    sys_dbs = ["performance_schema", "information_schema", "mysql", "sys"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list,
                                       opt_def_dict, multi_val=opt_multi_list)

    # Set JSON format for certain option settings
    if "-i" in args_array.keys() and "-m" in args_array.keys() \
       and "-j" not in args_array.keys():
        args_array["-j"] = True

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list):

        try:
            proglock = gen_class.ProgramLock(cmdline.argv,
                                             args_array.get("-y", ""))
            run_program(args_array, func_dict, sys_dbs=sys_dbs,
                        multi_val=opt_multi_list)
            del proglock

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for mysql_db_admin with id of: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())
