#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/_process_json.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/_process_non_json.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/help_message.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/analyze.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/check.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/checksum.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/detect_dbs.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/listdbs.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/optimize.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/process_request.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/proc_all_dbs.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/proc_all_tbls.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/proc_some_tbls.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/run_check.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/run_checksum.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/run_optimize.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/run_analyze.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/main.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/run_program.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/status.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
