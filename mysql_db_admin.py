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
                 [-m config_file -i db_name:table_name] |
                 [-e to_email [to_email2 ...] [-s subject_line] [-u]] |
                 [-z] [-p [-n N]]] |
             -A [db_name [db_name2 ...]] [-t table_name [table_name2 ...]] |
                 [-m config_file -i db_name:table_name] |
                 [-e to_email [to_email2 ...] [-s subject_line] [-u]] |
                 [-z] [-p [-n N]]] |
             -S [db_name [db_name2 ...]] [-t table_name [table_name2 ...]] |
                 [-m config_file -i db_name:table_name] |
                 [-e to_email [to_email2 ...] [-s subject_line] [-u]] |
                 [-z] [-p [-n N]]] |
             -D [db_name [db_name2 ...]] [-t table_name [table_name2 ...]] |
                 [-m config_file -i db_name:table_name] |
                 [-e to_email [to_email2 ...] [-s subject_line] [-u]] |
                 [-z] [-p [-n N]]] |
             -M [-m config_file -i [db_name:table_name]] |
                 [-e to_email [to_email2 ...] [-s subject_line] [-u]] |
                 [-z] [-p [-n N]]] |
             -L [-k]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c mysql_cfg => MySQL configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.

        -C [database name(s)] => Check a table for errors.
            -t table name(s) => Table names to check.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mysql_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -p => Expand the JSON format.
                -n N => Indentation for expanded JSON format.

        -A [database name(s)] => Analyze a table's key distribution, checks the
                table's indexes.
            -t table name(s) => Table names to check.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mysql_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -p => Expand the JSON format.
                -n N => Indentation for expanded JSON format.

        -S [database name(s)] => Return a checksum on a table.
            -t table name(s) => Table names to check.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mysql_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -p => Expand the JSON format.
                -n N => Indentation for expanded JSON format.

        -D [database name(s)] => Optimize/defragment a table, the command
                runs an Alter Table and Analyze command on the table.
            -t table name(s) => Table names to check.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mysql_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -p => Expand the JSON format.
                -n N => Indentation for expanded JSON format.

        -M => Display the current database status, such as uptime, memory
                use, connection usage, and status.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mysql_db_admin
            -o path/file => Directory path and file name for output.
                -w a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -p => Expand the JSON format.
                -n N => Indentation for expanded JSON format.

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
        NOTE 4:  -t option only works if passing in a single database name.

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

            If Mongo is set to use TLS or SSL connections, then one or more of
                the following entries will need to be completed to connect
                using TLS or SSL protocols.
                Note:  Read the configuration file to determine which entries
                    will need to be set.

                SSL:
                    auth_type = None
                    ssl_client_ca = None
                    ssl_client_key = None
                    ssl_client_cert = None
                    ssl_client_phrase = None
                TLS:
                    auth_type = None
                    tls_ca_certs = None
                    tls_certkey = None
                    tls_certkey_phrase = None

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

        Global variables:
            SYS_DBS -> Is a list of databases to be skipped under some options,
                but is overridden if set within the configration file
                (sys_dbs).

    Example:
        mysql_db_admin.py -c mysql -d config -D test -t users

"""

# Libraries and Global Variables
from __future__ import print_function
from __future__ import absolute_import

# Standard
import sys
import json
import pprint

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mysql_lib import mysql_class
    from .mysql_lib import mysql_libs
    from .mongo_lib import mongo_libs
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs
    import lib.gen_class as gen_class
    import mysql_lib.mysql_class as mysql_class
    import mysql_lib.mysql_libs as mysql_libs
    import mongo_lib.mongo_libs as mongo_libs
    import version

__version__ = version.__version__

# Global
SYS_DBS = ["performance_schema", "information_schema", "mysql", "sys"]


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def get_all_dbs_tbls(server, db_list, dict_key):

    """Function:  get_all_dbs_tbls

    Description:  Return a dictionary of databases with table lists.

    Arguments:
        (input) server -> Server instance
        (input) db_list -> List of database names
        (input) dict_key -> Dictionary key that is tuned to the Mysql version
        (output) db_dict -> Dictionary of databases and lists of tables

    """

    db_dict = dict()
    db_list = list(db_list)

    for dbs in db_list:
        tbl_list = gen_libs.dict_2_list(
            mysql_libs.fetch_tbl_dict(server, dbs), dict_key)
        db_dict[dbs] = tbl_list

    return db_dict


def get_db_tbl(server, args, db_list, **kwargs):

    """Function:  get_db_tbl

    Description:  Determines which databases and tables will be checked.

    Arguments:
        (input) server -> Server instance
        (input) args -> ArgParser class instance
        (input) db_list -> List of database names
        (input) **kwargs:
            sys_dbs -> List of system databases to skip
        (output) db_dict -> Dictionary of databases and lists of tables

    """

    db_dict = dict()
    db_list = list(db_list)
    dict_key = "TABLE_NAME" if server.version >= (8, 0) else "table_name"

    if db_list:
        db_list = gen_libs.del_not_and_list(
            db_list, kwargs.get("sys_dbs", list()))

        if not db_list:
            print("get_db_tbl 1: Warning:  No non-system databases to process")

        elif len(db_list) == 1 and args.get_val("-t"):
            db_tables = gen_libs.dict_2_list(
                mysql_libs.fetch_tbl_dict(server, db_list[0]), dict_key)
            tbl_list = gen_libs.del_not_in_list(args.get_val("-t"), db_tables)
            db_dict[db_list[0]] = tbl_list

        else:
            db_dict = get_all_dbs_tbls(server, db_list, dict_key)

    else:
        db_list = gen_libs.dict_2_list(
            mysql_libs.fetch_db_dict(server), "Database")
        db_list = gen_libs.del_not_and_list(
            db_list, kwargs.get("sys_dbs", list()))

        if not db_list:
            print("get_db_tbl 2: Warning:  No non-system databases to process")

        else:
            db_dict = get_all_dbs_tbls(server, db_list, dict_key)

    return db_dict


def get_json_template(server):

    """Function:  get_json_template

    Description:  Return a JSON template format.

    Arguments:
        (input) server -> Server instance
        (output) json_doc -> JSON filled-in template document

    """

    json_doc = dict()
    json_doc["Platform"] = "MySQL"
    json_doc["Server"] = server.name
    json_doc["AsOf"] = gen_libs.get_date() + "T" + gen_libs.get_time()

    return json_doc


def create_data_config(args):

    """Function:  create_data_config

    Description:  Create data_out config parameters.

    Arguments:
        (input) args -> ArgParser class instance
        (output) data_config -> Dictionary for data_out config parameters

    """

    data_config = dict()
    data_config["to_addr"] = args.get_val("-e")
    data_config["subj"] = args.get_val("-s")
    data_config["mailx"] = args.get_val("-u", def_val=False)
    data_config["outfile"] = args.get_val("-o")
    data_config["mode"] = args.get_val("-w", def_val="w")
    data_config["expand"] = args.get_val("-p", def_val=False)
    data_config["indent"] = args.get_val("-n")
    data_config["suppress"] = args.get_val("-z", def_val=False)
    data_config["mongo"] = gen_libs.load_module(
        args.get_val("-m"), args.get_val("-d"))
    data_config["db_tbl"] = args.get_val("-i")

    return data_config


def data_out(data, **kwargs):

    """Function:  data_out

    Description:  Outputs the data in a variety of formats and media.

    Arguments:
        (input) data -> JSON data document
        (input) kwargs:
            to_addr -> To email address
            subj -> Email subject line
            mailx -> True|False - Use mailx command
            outfile -> Name of output file name
            mode -> w|a => Write or append mode for file
            expand -> True|False - Expand the JSON format
            indent -> Indentation of JSON document if expanded
            suppress -> True|False - Suppress standard out
            mongo -> Mongo server configuration - Insert into Mongo database
            db_tbl -> database:table - Database name:Table name
        (output) state -> True|False - Successful operation
        (output) msg -> None or error message

    """

    state = True
    msg = None

    if not isinstance(data, dict):
        return False, "Error: Is not a dictionary: %s" % (data)

    mail = None
    data = dict(data)
    cfg = {"indent": kwargs.get("indent", 4)} if kwargs.get("indent", False) \
        else dict()

    if kwargs.get("to_addr", False):
        subj = kwargs.get("subj", "NoSubjectLinePassed")
        mail = gen_class.setup_mail(kwargs.get("to_addr"), subj=subj)
        mail.add_2_msg(json.dumps(data, **cfg))
        mail.send_mail(use_mailx=kwargs.get("mailx", False))

    if kwargs.get("outfile", False):
        outfile = open(kwargs.get("outfile"), kwargs.get("mode", "w"))
        pprint.pprint(data, stream=outfile, **cfg)

    if not kwargs.get("suppress", False):
        if kwargs.get("expand", False):
            pprint.pprint(data, **cfg)

        else:
            print(data)

    if kwargs.get("mongo", False):
        dbs, tbl = kwargs.get("db_tbl").split(":")
        state, msg = mongo_libs.ins_doc(kwargs.get("mongo"), dbs, tbl, data)

    return state, msg


def analyze(server, args, **kwargs):

    """Function:  analyze

    Description:  Analzye the tables for problems.

    Arguments:
        (input) server -> Server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            sys_dbs -> List of system databases to skip

    """

    db_list = list(args.get_val("-A"))
    db_dict = get_db_tbl(server, args, db_list, **kwargs)
    results = get_json_template(server)
    results["Type"] = "analyze"
    results["Results"] = list()
    data_config = dict(create_data_config(args))

    for dbn in db_dict:
        t_results = {"Database": dbn, "Tables": list()}

        for tbl in db_dict[dbn]:
            t_data = {"TableName": tbl}

            for data in mysql_libs.analyze_tbl(server, dbn, tbl):
                t_data[gen_libs.pascalize(data["Msg_type"])] = data["Msg_text"]

            t_results["Tables"].append(t_data)

        results["Results"].append(t_results)

    state = data_out(results, **data_config)

    if not state[0]:
        print("analyze: Error encountered: %s" % (state[1]))


def check(server, args, **kwargs):

    """Function:  check

    Description:  Check the tables for errors.

    Arguments:
        (input) server -> Server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            sys_dbs -> List of system databases to skip

    """

    db_list = list(args.get_val("-C"))
    db_dict = get_db_tbl(server, args, db_list, **kwargs)
    results = get_json_template(server)
    results["Type"] = "check"
    results["Results"] = list()
    data_config = dict(create_data_config(args))

    for dbn in db_dict:
        t_results = {"Database": dbn, "Tables": list()}

        for tbl in db_dict[dbn]:
            t_data = {"TableName": tbl}

            for data in mysql_libs.check_tbl(server, dbn, tbl):
                t_data[gen_libs.pascalize(data["Msg_type"])] = data["Msg_text"]

            t_results["Tables"].append(t_data)

        results["Results"].append(t_results)

    state = data_out(results, **data_config)

    if not state[0]:
        print("check: Error encountered: %s" % (state[1]))


def optimize(server, args, **kwargs):

    """Function:  optimize

    Description:  Optimizes the tables for best performance.

    Arguments:
        (input) server -> Server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            sys_dbs -> List of system databases to skip

    """

    db_list = list(args.get_val("-D"))
    db_dict = get_db_tbl(server, args, db_list, **kwargs)
    results = get_json_template(server)
    results["Type"] = "optimize"
    results["Results"] = list()
    data_config = dict(create_data_config(args))

    for dbn in db_dict:
        t_results = {"Database": dbn, "Tables": list()}

        for tbl in db_dict[dbn]:
            t_data = {"TableName": tbl}

            for data in mysql_libs.optimize_tbl(server, dbn, tbl):
                t_data[gen_libs.pascalize(data["Msg_type"])] = data["Msg_text"]

            t_results["Tables"].append(t_data)

        results["Results"].append(t_results)

    state = data_out(results, **data_config)

    if not state[0]:
        print("optimize: Error encountered: %s" % (state[1]))


def checksum(server, args, **kwargs):

    """Function:  checksum

    Description:  Returns checksums of the tables.

    Arguments:
        (input) server -> Server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            sys_dbs -> List of system databases to skip

    """

    db_list = list(args.get_val("-S"))
    db_dict = get_db_tbl(server, args, db_list, **kwargs)
    results = get_json_template(server)
    results["Type"] = "checksum"
    results["Results"] = list()
    data_config = dict(create_data_config(args))

    for dbn in db_dict:
        t_results = {"Database": dbn, "Tables": list()}

        for tbl in db_dict[dbn]:
            t_data = {"TableName": tbl}

            for data in mysql_libs.checksum(server, dbn, tbl):
                t_data["Checksum"] = data["Checksum"]

            t_results["Tables"].append(t_data)

        results["Results"].append(t_results)

    state = data_out(results, **data_config)

    if not state[0]:
        print("optimize: Error encountered: %s" % (state[1]))


def status(server, args, **kwargs):

    """Function:  status

    Description:  Retrieves a number of database status variables and sends
        them out either in standard out (print) or to a JSON format which
        is printed and poissibly inserted into a Mongo database.

    Arguments:
        (input) server -> Server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            sys_dbs -> List of system databases to skip

    """

    server.upd_srv_stat()
    results = get_json_template(server)
    results["Type"] = "status"
    data_config = dict(create_data_config(args))
    results["Memory"] = {
        "CurrentUsage": server.cur_mem_mb, "MaxUsage": server.max_mem_mb,
        "PercentUsed": server.prct_mem}
    results["UpTime"] = server.days_up
    results["Connections"] = {
        "CurrentConnected": server.cur_conn, "MaxConnections": server.max_conn,
        "PercentUsed": server.prct_conn}
    state = data_out(results, **data_config)

    if not state[0]:
        print("analyze: Error encountered: %s" % (state[1]))


def listdbs(server, args, **kwargs):

    """Function:  listdbs

    Description:  List user or user/system databases in the database instance.

    Arguments:
        (input) server -> Server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            sys_dbs -> List of system databases

    """

    sys_dbs = list(kwargs.get("sys_dbs", []))
    db_list = gen_libs.dict_2_list(mysql_libs.fetch_db_dict(server),
                                   "Database")

    if args.arg_exist("-k"):
        print("List of user and system databases:")

        for item in db_list:
            print("    %s" % (item))

    else:
        print("List of user databases:")

        for item in gen_libs.del_not_and_list(db_list, sys_dbs):
            print("    %s" % (item))


def run_program(args, func_dict):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary of functions

    """

    global SYS_DBS

    func_dict = dict(func_dict)
    server = mysql_libs.create_instance(
        args.get_val("-c"), args.get_val("-d"), mysql_class.Server)
    server.connect(silent=True)

    if server.conn_msg:
        print("run_program:  Error encountered on server(%s):  %s" %
              (server.name, server.conn_msg))

    else:
        # Intersect args.args_array & func_dict to determine functions to call
        for item in set(args.get_args_keys()) & set(func_dict.keys()):
            cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
            sys_dbs = cfg.sys_dbs if hasattr(cfg, "sys_dbs") else SYS_DBS
            func_dict[item](server, args, sys_dbs=sys_dbs)

        mysql_libs.disconnect(server)


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> directory check options and their perms in octal
        file_perms -> file check options with their perms in octal
        file_crt_list -> contains options which require files to be created
        func_dict -> dictionary list for the function calls or other options
        opt_con_req_list -> contains the options that require other options
        opt_def_dict -> contains options with their default values
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values
        opt_xor_dict -> contains options which are XOR with its values

    Arguments:
        (input) argv -> arguments from the command line

    """

    dir_perms_chk = {"-d": 5}
    file_perms = {"-o": 6}
    file_crt_list = ["-o"]
    func_dict = {
        "-A": analyze, "-C": check, "-D": optimize, "-S": checksum,
        "-M": status, "-L": listdbs}
    opt_con_req_list = {"-i": ["-m"], "-s": ["-e"], "-u": ["-e"], "-w": ["-o"]}
    opt_def_dict = {
        "-t": None, "-A": [], "-C": [], "-D": [], "-S": [], "-n": 4,
        "-i": "sysmon:mysql_db_admin"}
    opt_multi_list = ["-A", "-C", "-D", "-S", "-t", "-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = [
        "-c", "-d", "-t", "-A", "-C", "-D", "-S", "-i", "-m", "-o", "-e", "-s",
        "-y", "-w", "-n"]
    opt_xor_dict = {
        "-A": ["-C", "-D", "-M", "-S", "-L"],
        "-C": ["-A", "-D", "-M", "-S", "-L"],
        "-D": ["-A", "-C", "-M", "-S", "-L"],
        "-S": ["-A", "-C", "-D", "-M", "-L"],
        "-M": ["-A", "-C", "-D", "-S", "-L"],
        "-L": ["-A", "-C", "-D", "-S", "-M"]}

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, multi_val=opt_multi_list,
        opt_def=opt_def_dict)

    if args.arg_parse2()                                                    \
       and not gen_libs.help_func(args, __version__, help_message)          \
       and args.arg_require(opt_req=opt_req_list)                           \
       and args.arg_xor_dict(opt_xor_val=opt_xor_dict)                      \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)                  \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)                    \
       and args.arg_file_chk(file_perm_chk=file_perms, file_crt=file_crt_list):

        try:
            proglock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(args, func_dict)
            del proglock

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for mysql_db_admin with id of: %s"
                  % (args.get_val("-y", def_val="")))


if __name__ == "__main__":
    sys.exit(main())
