# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.1.2] - 2020-06-10
### Fixed
- status:  Added email capability for non-json format.
- status:  Added write to file capability for non-json format.

### Changed
- status:  Replaced section code with call to \_process_non_json function.
- status:  Added standard out suppression for non-json format.
- status:  Moved the initialization of the dictionary structure to outside of the if statement.
- run_check:  Using global variable for template printing.
- run_optimize:  Using global variable for template printing.
- run_analyze:  Using global variable for template printing.

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
- status:  Converted JSON output to CamelCase.
- run_check:  Reformatted output.
- run_optimize:  Reformatted output.
- run_checksum:  Reformatted output.
- run_analyze:  Reformatted output.
- status:  Refactored function to reduce program complexity.
- run_program: Changed variable name to standard naming convention.
- status: Changed variable name to standard naming convention.
- \_proc_some_tbls: Changed variable name to standard naming convention.
- \_proc_all_tbls: Changed variable name to standard naming convention.
- \_proc_all_dbs: Changed variable name to standard naming convention.
- run_check: Changed variable name to standard naming convention.
- run_optimize: Changed variable name to standard naming convention.
- run_checksum: Changed variable name to standard naming convention.
- run_analyze: Changed variable name to standard naming convention.
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
- run_analyze:  Fixed problem with mutable default arguments issue.
- run_optimize:  Fixed problem with mutable default arguments issue.

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
- run_program:  Fixed problem with mutable default arguments issue.
- status:  Fixed problem with mutable default arguments issue.
- check:  Fixed problem with mutable default arguments issue.
- optimize:  Fixed problem with mutable default arguments issue.
- checksum:  Fixed problem with mutable default arguments issue.
- analyze:  Fixed problem with mutable default arguments issue.
- process_request:  Fixed problem with mutable default arguments issue.
- detect_dbs:  Fixed problem with mutable default arguments issue.

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
- Changed "mongo_libs" calls to new naming schema.
- Changed "mysql_libs" calls to new naming schema.
- Changed "cmds_gen" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
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
- Run_Check:  Changed print to use format option.
- Run_Optimize:  Changed print to use format option.
- Run_Checksum:  Changed print to use format option.
- Run_Analyze:  Changed print to use format option.


## [1.3.0] - 2016-09-15
### Changed
- Run_Analyze:  Changed the way the system databases validated and skipped for the function.
- Run_Optimize:  Changed the way the system databases validated and skipped for the function.
- main:  Create list of system databases and pass to other functions.


## [1.2.0] - 2016-04-15
### Changed
- Run_Program:  Processing for some of the new options and passing to the functions.  Setup a Mongo instance.
- main:  Added options "-M", "-m", "-f", "-i", and "-o" options to a number of variables and added a number of new function call checks.
- Optimize:  Pass \*\*kwargs to Process_Request function call.
- Checksum:  Pass \*\*kwargs to Process_Request function call.
- Analyze:  Pass \*\*kwargs to Process_Request function call.
- Check:  Pass \*\*kwargs to Process_Request function call.
- Process_Request:  Receive \*\*kwargs into function and passed \*\*kwargs to Run_Check, Run_Analyze, Run_Checksum, and Run_Optimize functions.

### Added
- Status function.


## [1.1.0] - 2016-04-04
### Changed
- Run_Analyze:  Per MySQL Reference documentation, no system database should be analyzed or optimized.  Removing "mysql", "information_schema", and "performance_schema" from the check.
- Run_Optimize:  Per MySQL Reference documentation, no system database should be analyzed or optimized.  Removing "mysql", "information_schema", and "performance_schema" from the check.


## [1.0.0] - 2016-04-01
- Initial creation.

