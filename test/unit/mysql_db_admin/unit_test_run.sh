#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
test/unit/mysql_db_admin/_process_non_json.py
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
