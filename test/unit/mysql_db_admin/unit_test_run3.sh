#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python3 ./test/unit/mysql_db_admin/_process_json.py
/usr/bin/python3 ./test/unit/mysql_db_admin/_process_non_json.py
/usr/bin/python3 ./test/unit/mysql_db_admin/help_message.py
/usr/bin/python3 ./test/unit/mysql_db_admin/analyze.py
/usr/bin/python3 ./test/unit/mysql_db_admin/check.py
/usr/bin/python3 ./test/unit/mysql_db_admin/checksum.py
/usr/bin/python3 ./test/unit/mysql_db_admin/detect_dbs.py
/usr/bin/python3 ./test/unit/mysql_db_admin/listdbs.py
/usr/bin/python3 ./test/unit/mysql_db_admin/optimize.py
/usr/bin/python3 ./test/unit/mysql_db_admin/process_request.py
/usr/bin/python3 ./test/unit/mysql_db_admin/proc_all_dbs.py
/usr/bin/python3 ./test/unit/mysql_db_admin/proc_all_tbls.py
/usr/bin/python3 ./test/unit/mysql_db_admin/proc_some_tbls.py
/usr/bin/python3 ./test/unit/mysql_db_admin/run_check.py
/usr/bin/python3 ./test/unit/mysql_db_admin/run_checksum.py
/usr/bin/python3 ./test/unit/mysql_db_admin/run_optimize.py
/usr/bin/python3 ./test/unit/mysql_db_admin/run_analyze.py
/usr/bin/python3 ./test/unit/mysql_db_admin/status.py
/usr/bin/python3 ./test/unit/mysql_db_admin/run_program.py
/usr/bin/python3 ./test/unit/mysql_db_admin/main.py
