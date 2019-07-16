# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


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

