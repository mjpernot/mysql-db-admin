#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/help_message.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/analyze.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/check.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/checksum.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/create_data_config.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/data_out.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/get_all_dbs_tbls.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/get_db_tbl.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/get_json_template.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/listdbs.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/optimize.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/main.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/run_program.py
coverage run -a --source=mysql_db_admin test/unit/mysql_db_admin/status.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
