# Python project for administration in a MySQL database.
# Classification (U)

# Description:
  Used for database administration of a MySQL database to include compacting/defraging a table, checking a table for errors, analyze a table's key distribution (index check), and get a checksum on a table.


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
  * Send output to standard out or file.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python3-pip
    - python3-devel
    - gcc


# Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-db-admin.git
```

Install/upgrade system modules.

Install supporting classes and libraries.

NOTE: Install as the user that will run the program.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting classes and libraries.

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-mysql-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Configuration:

Create MySQL configuration file and make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "MYSQL_DIRECTORY/mysqld.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

  * If SSL connections are being used, configure one or more of these entries:
    - ssl_client_ca = None
    - ssl_client_key = None
    - ssl_client_cert = None

  * Only changes these if necessary and have knowledge in MySQL SSL configuration setup:
    - ssl_client_flag = None
    - ssl_disabled = False
    - ssl_verify_id = False
    - ssl_verify_cert = False

  * TLS version: Set what TLS versions are allowed in the connection set up.
    - tls_versions = []

```
cp config/mysql_cfg.py.TEMPLATE config/mysql_cfg.py
vim config/mysql_cfg.py
chmod 600 config/mysql_cfg.py
```

Create MySQL definition file and make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
  * Note:  socket use is only required to be set in certain conditions when connecting using localhost.
    - password="PSWORD"
    - socket=DIRECTORY_PATH/mysqld.sock

```
cp config/mysql.cfg.TEMPLATE config/mysql.cfg
vim config/mysql.cfg
chmod 600 config/mysql.cfg
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
mysql_db_admin.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
test/unit/mysql_db_admin/unit_test_run.sh
test/unit/mysql_db_admin/code_coverage.sh
```

