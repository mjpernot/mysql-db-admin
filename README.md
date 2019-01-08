# Python project for administration in a MySQL database.
# Classification (U)

# Description:
  This program is used to do database administration in a MySQL database to include compacting/defraging a table, checking a table for errors, analyze a table's key distribution (index check), and get a checksum on a table.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Check a table for errors.
  * Analyze a table's key distribution (checks the table's indexes).
  * Return a checksum on a table.
  * Optimize/defragment a table.
  * Display the current database status, such as uptime, memory use, connection usage, and status.
  * Send output to standard out, file, or insert into a Mongo database collection.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mysql_lib/mysql_libs
    - mysql_lib/mysql_class
    - mongo_lib/mongo_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-db-admin.git
```

Install/upgrade system modules.

```
cd mysql-db-admin
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:
  * Replace **{Python_Project}** with the baseline path of the python program.

Create MySQL configuration file.

```
cd config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - passwd = "ROOT_PASSWORD"
    - host = "SERVER_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "{Python_Project}/config/mysql.cfg"

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

```
cp mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```


# Program Descriptions:
### Program: mysql_db_admin.py
##### Description: Administration program for the MySQL binary log system.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mysql-db-admin/mysql_db_admin.py -h
```


# Help Message:
  Below is the help message for the program the program.  Run the program with the -h option get the latest help message for the program.

    Program:  mysql_db_admin.py

    Description:  A MySQL Database Administration program that can run a number
        of different administration functions such as compacting/defraging a
        table, checking a table for errors, analyze a table's key distribution
        (index check), or get a checksum on a table.  The options will allow
        for for a single object, multiple objects, or all objects.  Also can
        return the database's status to include uptime, connection usage,
        memory use, and database server status.

    Usage:
        mysql_db_admin.py -c file -d path {-C [db_name [db_name ...]]
            |-A [db_name [db_name ...] | -S [db_name [db_name ...]]
            |-D [db_name [db_name ...]] | -M {-j
            |-i {db_name:table_name} | -m file} | -o dir_path/file}}
            [-t [table_name [table_name ...]]] [-v | -h]

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


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mysql_db_admin.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-db-admin.git
```

Install/upgrade system modules.

```
cd mysql-db-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mysql_db_admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-db-admin
```

### Unit:  help_message
```
test/unit/mysql_db_admin/help_message.py
```

### Unit:  
```
test/unit/mysql_db_admin/
```

### Unit:  
```
test/unit/mysql_db_admin/
```

### Unit:  run_program
```
test/unit/mysql_db_admin/run_program.py
```

### Unit:  main
```
test/unit/mysql_db_admin/main.py
```

### All unit testing
```
test/unit/mysql_db_admin/unit_test_run.sh
```

### Code coverage program
```
test/unit/mysql_db_admin/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mysql_db_admin.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-db-admin.git
```

Install/upgrade system modules.

```
cd mysql-db-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create MySQL configuration file.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd test/integration/mysql_db_admin/config
cp ../../../../config/mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup.
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - sid = SERVER_ID
    - extra_def_file = '{Python_Project}/config/mysql.cfg'

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.
```
cp ../../../../config/mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the MySQL definition setup.
  * Change these entries in the MySQL configuration file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```


# Integration test runs for mysql_db_admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-db-admin
```


### Integration:  
```
test/integration/mysql_db_admin/
```

### All integration testing
```
test/integration/mysql_db_admin/integration_test_run.sh
```

### Code coverage program
```
test/integration/mysql_db_admin/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mysql_db_admin.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-db-admin.git
```

Install/upgrade system modules.

```
cd mysql-db-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:
  * Replace **{Python_Project}** with the baseline path of the python program.

Create MySQL configuration file.

```
cd test/blackbox/mysql_db_admin/config
cp ../../../../config/mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - sid = SERVER_ID
    - extra_def_file = '{Python_Project}/config/mysql.cfg'

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

```
cp ../../../../config/mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the MySQL definition setup.
  * Change these entries in the MySQL configuration file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```

# Blackbox test run for mysql_db_admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-db-admin
```

### Blackbox:  
```
test/blackbox/mysql_db_admin/blackbox_test.sh
```

