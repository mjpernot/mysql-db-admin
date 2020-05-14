# Python project for administration in a MySQL database.
# Classification (U)

# Description:
  This program is used to do database administration in a MySQL database to include compacting/defraging a table, checking a table for errors, analyze a table's key distribution (index check), and get a checksum on a table.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features:
  * Check a table for errors.
  * Analyze a table's key distribution (checks the table's indexes).
  * Return a checksum on a table.
  * Optimize/defragment a table.
  * Display the current database status, such as uptime, memory use, connection usage, and status.
  * Send output to standard out, file, or insert into a Mongo database collection.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
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
  * Replace **PYTHON_PROJECT** with the baseline path of the python program.

Create MySQL configuration file.

```
cd config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "SERVER_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

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
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```

Create Mongodb configuration file.
  * If submitting output to Mongo database, then require a Mongodb configuration file.

```
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"

  * Change these entries only if required:
    - port = 27017
    - conf_file = None
    - auth = True

  * If connecting to a Mongo replica set:
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mysql-db-admin/mysql_db_admin.py -h
```


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
test/unit/mysql_db_admin/help_message.py
test/unit/mysql_db_admin/analyze.py
test/unit/mysql_db_admin/check.py
test/unit/mysql_db_admin/checksum.py
test/unit/mysql_db_admin/detect_dbs.py
test/unit/mysql_db_admin/optimize.py
test/unit/mysql_db_admin/process_request.py
test/unit/mysql_db_admin/proc_all_dbs.py
test/unit/mysql_db_admin/proc_all_tbls.py
test/unit/mysql_db_admin/proc_some_tbls.py
test/unit/mysql_db_admin/run_check.py
test/unit/mysql_db_admin/run_checksum.py
test/unit/mysql_db_admin/run_optimize.py
test/unit/mysql_db_admin/run_analyze.py
test/unit/mysql_db_admin/status.py
test/unit/mysql_db_admin/run_program.py
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

