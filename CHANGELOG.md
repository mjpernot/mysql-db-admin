# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.

## [5.1.0] - 2025-04-15
- Removed support for any pre-MySQL 8.0 versions.
- Updated python-lib v4.0.1
- Updated mysql-lib v5.5.0

### Changed
- get_db_tbl: Removed check for pre-MySQL v8.0 when setting dict_key variable.
- data_out: Added default of "w" mode for gen_libs.write_file call.
- Documentation updates.

### Removed
- Support for MySQL 5.6/5.7


## [5.0.0] - 2024-12-03
Breaking Changes

- Removed support for Python 2.7.
- Removed Mongo insert option.
- Updated mysql-lib v5.4.0
- Updated python-lib v4.0.0

### Fixed
- data_out:  Added call to gen_libs.write_file to write flatten JSON objects.

### Changed
- data_out: Replaced open call with a "with open" call.
- create_data_config, data_out: Removed Mongo code.
- Replaced dict() with {} and list() with [].
- Converted strings to f-strings.
- Documentation changes.

### Deprecated
- Support for MySQL 5.6/5.7


## [4.0.5] - 2024-11-18
- Updated python-lib to v3.0.8
- Updated mysql-lib to v5.3.9
- Updated mongo-lib to v4.3.4

### Fixed
- Set chardet==3.0.4 for Python 3.

### Deprecated
- Support for Python 2.7


## [4.0.4] - 2024-11-07
- Updated chardet==4.0.0 for Python 3
- Updated distro==1.9.0 for Python 3
- Updated protobuf==3.19.6 for Python 3
- Updated mysql-connector-python==8.0.28 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated mongo-lib to v4.3.3
- Updated mysql-lib to v5.3.8
- Updated python-lib to v3.0.7


## [4.0.3] - 2024-09-27
- Updated pymongo==4.1.1 for Python 3.6
- Updated simplejson==3.13.2 for Python 3
- Updated mongo-lib to v4.3.2
- Updated python-lib to v3.0.5
- Updated mysql-lib to v5.3.7


## [4.0.2] - 2024-08-19
- Updated simplejson to 3.13.2 for Python 2.

### Fixed
- create_data_config:  Only set "mongo" entry if mongo config file is passed.


## [4.0.1] - 2024-07-23

### Fixed
- create_data_config: Set mongo entry to the Mongo configuration.

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [4.0.0] - 2024-04-24
Breaking Change

- Change output to a JSON format.
- Add ability to email, insert into Mongo, save to file and/or display to standard out.

### Added
- data_out: Outputs the data in a variety of formats and media.
- create_data_config: Create data_out config parameters.
- get_json_template: Return a JSON template format.
- get_all_dbs_tbls: Return a dictionary of databases with table lists.
- get_db_tbl: Determines which databases and tables will be checked.

### Changed
- config/mongo.py.TEMPLATE: Added sys_dbs entry for system database list.
- main: Added -n and -p options, removed the check for converting to JSON if -m option is used.
- analyze, check, optimize, checksum: Refactored to change output to JSON format and additional options for sending out.
- Documentation updates.

### Removed
- \_process_non_json
- \_process_json
- detect_dbs
- process_request
- \_proc_all_dbs
- \_proc_all_tbls
- \_proc_some_tbls
- run_checksum
- run_optimize
- run_check
- run_analyze


## [3.3.4] - 2024-04-23
- Updated mongo-lib to v4.3.0
- Added TLS capability for Mongo
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- config/mongo.py.TEMPLATE: Added TLS entries.
- Documentation updates.


## [3.3.3] - 2024-03-12

### Changed
- run_program: Read in configuration module and set the sys_dbs variable.
- main: Moved the sys_dbs variable to the global SYS_DBS variable.


## [3.3.2] - 2024-02-26
- Updated to work in Red Hat 8
- Updated mysql-lib to v5.3.4
- Updated mongo-lib to v4.2.9
- Updated python-lib to v3.0.3

### Changed
- main:  Removed the gen_libs.get_inst call and changed gen_libs.help_func to use the gen_class.ArgParser parameter format.
- detect_dbs:  Removed \*\*kwargs from parameter list, no longer required.
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [3.3.1] - 2022-10-12
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mysql-lib to v5.3.2
- Upgraded mongo-lib to v4.2.2

### Changed
- \_process_non_json:  Converted dictionary items call to a list.
- Converted imports to use Python 2.7 or Python 3.


## [3.3.0] - 2022-08-16
- Upgraded python-lib to v2.9.3
- Replaced args_parser module with the gen_class.ArgParser class.

### Changed
- Multiple functions: Replaced the use of arg_parser (args_array) with gen_class.ArgParser class (args).


## [3.2.1] - 2022-07-12
- Upgraded python-lib to v2.9.2
- Upgraded mysql-lib to v5.3.1
- Upgraded mongo-lib to v4.2.1
- Added TLS capability

### Changed
- config/mysql_cfg.py.TEMPLATE: Added TLS version entry.
- config/mongo.py.TEMPLATE: Removed old entries.
- Documentation updates.


## [3.2.0] - 2021-08-17
- Updated to work in MySQL 8.0 and 5.7 environments.
- Updated to work in a SSL environment.
- Updated to use the mysql_libs v5.2.2 library.

### Changed
- \_proc_all_dbs, \_proc_all_tbls, \_proc_some_tbls:  Added dict_key to argument list and to fetch_tbl_dict call.
- process_request:  Set dictionary key based on MySQL version and refactored a number of if/else statements.
- config/mongo.py.TEMPLATE: Added SSL configuration options.
- config/mysql_cfg.py.TEMPLATE: Added SSL configuration options.
- config/mysql.cfg.TEMPLATE:  Point to correct socket file.
- Documentation updates.


## [3.1.3] - 2020-11-21
- Updated to use the mysql_libs v5.0.4 library.
- Updated to use pymongo v3.8.0.
- Updated to be used in FIPS 140-2 environment.
- Updated to use python_lib v2.8.3 to use mailx capability.

### Fixed
- Allow to override the default sendmail (postfix) and use mailx command.
- config/mysql.cfg.TEMPLATE:  Point to correct socket file.

### Added
- Added -L option to list databases in the database instance.
- listdbs:  List user or user/system databases in the database instance.
- \_process_json:  Private function for status to process json format data.

### Changed
- main:  Added system database "sys" to sys_dbs setting.
- main:  Added -L option to the argument checks.
- status: Refactored the function.
- main:  Set "-j" option to args_array if "-i" and "-m" options are present.
- \_process_non_json, status:  Determine whether to use sendmail or mailx when using the mail option.
- main:  Added -u option to allow override of sendmail and use mailx.
- run_program:  Process status connection on MySQL connection call.
- status:  Processed status return from mongo_libs.ins_doc call.
- run_program:  Replaced cmds_gen.disconnect with mysql_libs.disconnect call.
- config/mongo.py.TEMPLATE:  Changed configuration entry and added a number of configuration entries.
- config/mysql_cfg.py.TEMPLATE:  Changed configuration entry.
- Documentation updates.

### Removed
- mysql_libs.cmds_gen module.


## [3.1.2] - 2020-06-10
### Fixed
- status:  Added email capability for non-json format.
- status:  Added write to file capability for non-json format.

### Changed
- status:  Replaced section code with call to \_process_non_json function.
- status:  Added standard out suppression for non-json format.
- status:  Moved the initialization of the dictionary structure to outside of the if statement.
- run_optimize, run_analyze, run_check:  Using global variable for template printing.

### Added
- \_process_non_json:  Private function for status to process non-json format data.
- Added global variable for template printing.


## [3.1.1] - 2020-05-14
### Added
- Added -y option to allow for unique Program Lock flavor IDs.
- Added -f option to Flatten the JSON data structure to file and standard out.
- Added -a option to allow for append of data to an existing output file.

### Fixed:
- main:  Fixed handling command line arguments from SonarQube scan finding.

### Changed
- status:  Converted JSON output to PascalCase.
- run_optimize, run_checksum, run_analyze, run_check:  Reformatted output.
- status:  Refactored function to reduce program complexity.
- Changed variable name to standard naming convention in multiple functions.
- main: Added -y option setting to the ProgramLock setup.
- status:  Added flattening of JSON structure to standard out and to file.
- status:  Added file mode option to writing data to a file.  Default is write.
- config/mongo.py.TEMPLATE:  Changed to generic setup.
- config/mysql.cfg.TEMPLATE:  Changed to generic setup.
- config/mysql_cfg.py.TEMPLATE:  Changed to generic setup.
- Documentation updates.

### Removed
- Removed non-used library modules.


## [3.1.0] - 2019-12-06
### Fixed
- run_optimize, run_analyze:  Fixed problem with mutable default arguments issue.

### Added
- Added a program lock mechanism to the program.
- Added -z option for standard out suppression.

### Changed
- main:  Added gen_class.ProgramLock class and code check.
- run_program:  Replaced setup_mail call with gen_class.setup_mail call.
- status:  Added print JSON format to standard out, unless standard out is suppressed.
- Documentation update.

### Removed
- setup_mail:  No longer required, replaced with call to gen_class.setup_mail.


## [3.0.0] - 2019-07-16
Breaking Change

- Modified program to use the mysql_class v4.0.0 version.  The v4.0.0 replaces the MySQLdb support library with the mysql.connector support library.

### Fixed
- Fixed problem with mutable default arguments issue in multiple functions.

### Changed
- status:  Added capability to mail out JSON formatted data.
- run_program:  Added setup of mail instance and passing mail instance to functions.
- main:  Added '-e' and '-s' options to allow for email capability for some options.
- status:  Removed "mongo_libs.json_prt_ins_2_db" and replaced with own internal code to do the same thing.
- status:  Converted JSON document to using camelCase for keys.
- process_request:  Replaced sections of code with calls to \_proc_some_tbls, \_proc_all_dbs, and \_proc_all_tbls.

### Added
- setup_mail:  Initialize a mail instance.
- \_proc_some_tbls:  Private function for process_request.  Process some tables in listed databases.
- \_proc_all_tbls:  Private function for process_request.  Process all tables.
- \_proc_all_dbs:  Private function for process_request.  Process all tables in listed databases.


## [2.0.1] - 2018-12-06
### Fixed
- process_request:  Changed function parameter mutable argument default to immutable argument default.


## [2.0.0] - 2018-05-23
Breaking Change

### Changed
- Changed "mongo_libs", "mysql_libs", "cmds_gen", "gen_libs", and "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [1.7.0] - 2018-05-08
### Changed
- Changed "server" to "mysql_class" module reference.
- Changed "commands" to "mysql_libs" module reference.
- Changed "cmds_mongo" to "mongo_libs" module reference.

### Added
- Added single-source version control.


## [1.6.0] - 2017-08-18
### Changed
- Convert program to use local libraries from ./lib directory.
- Change single quotes to double quotes.
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.


## [1.5.0] - 2016-12-20
### Changed
- Status:  Changed the way output format is handled in a number of 'if' statements.  Assume standard output unless the -j option is set in args_array.
- main:  Changed the -A, -C, -D, -S, and -t options so they can accept multiple values or an empty list (all).  Replaced -f option with -j; the default output will be standard out unless -j option is selected for JSON format.
- Process_Request:  Removed "all" checks from 'if' statements.  Instead an empty list means to process all databases or tables.  Reorganized the checks to use intersetions and differences of sets to determine which databases and tables to process.


## [1.4.0] - 2016-12-15
### Changed
- Run_Optimize, Run_Checksum, Run_Analyze, Run_Check:  Changed print to use format option.


## [1.3.0] - 2016-09-15
### Changed
- Run_Optimize, Run_Analyze:  Changed the way the system databases validated and skipped for the function.
- main:  Create list of system databases and pass to other functions.


## [1.2.0] - 2016-04-15
### Changed
- Run_Program:  Processing for some of the new options and passing to the functions.  Setup a Mongo instance.
- main:  Added options "-M", "-m", "-f", "-i", and "-o" options to a number of variables and added a number of new function call checks.
- Checksum, Analyze, Check, Optimize:  Pass \*\*kwargs to Process_Request function call.
- Process_Request:  Receive \*\*kwargs into function and passed \*\*kwargs to Run_Check, Run_Analyze, Run_Checksum, and Run_Optimize functions.

### Added
- Status function.


## [1.1.0] - 2016-04-04
### Changed
- Run_Optimize, Run_Analyze:  Per MySQL Reference documentation, no system database should be analyzed or optimized.  Removing "mysql", "information_schema", and "performance_schema" from the check.


## [1.0.0] - 2016-04-01
- Initial creation.

