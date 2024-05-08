#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python ./test/unit/mysql_db_admin/_process_json.py
/usr/bin/python ./test/unit/mysql_db_admin/_process_non_json.py
/usr/bin/python ./test/unit/mysql_db_admin/help_message.py
/usr/bin/python ./test/unit/mysql_db_admin/analyze.py
/usr/bin/python ./test/unit/mysql_db_admin/check.py
/usr/bin/python ./test/unit/mysql_db_admin/checksum.py
/usr/bin/python ./test/unit/mysql_db_admin/create_data_config.py
/usr/bin/python ./test/unit/mysql_db_admin/data_out.py
/usr/bin/python ./test/unit/mysql_db_admin/get_all_dbs_tbls.py
/usr/bin/python ./test/unit/mysql_db_admin/get_db_tbl.py
/usr/bin/python ./test/unit/mysql_db_admin/get_json_template.py
/usr/bin/python ./test/unit/mysql_db_admin/listdbs.py
/usr/bin/python ./test/unit/mysql_db_admin/optimize.py
/usr/bin/python ./test/unit/mysql_db_admin/status.py
/usr/bin/python ./test/unit/mysql_db_admin/run_program.py
/usr/bin/python ./test/unit/mysql_db_admin/main.py
