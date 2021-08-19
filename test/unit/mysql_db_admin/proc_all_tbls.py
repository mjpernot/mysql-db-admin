#!/usr/bin/python
# Classification (U)

"""Program:  proc_all_tbls.py

    Description:  Unit testing of _proc_all_tbls in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/proc_all_tbls.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_admin
import version

__version__ = version.__version__


def func_holder(server, dbs, tbl):

    """Method:  func_holder

    Description:  Function stub holder for a generic function call.

    Arguments:
        server
        dbs
        tbl

    """

    status = True

    if server and dbs and tbl:
        status = True

    return status


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mysql_80
        test_pre_mysql_80
        test_no_tbls2
        test_no_tbls
        test_some_tbls
        test_all_tbls

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.func_name = func_holder
        self.db_list = ["db1", "db2"]
        self.db_name = ["db1", "db2"]
        self.db_name2 = ["db1"]
        self.db_name3 = []
        self.db_name4 = ["db3"]
        self.version = {"version": "5.7"}
        self.version2 = {"version": "8.0"}

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_mysql_80(self, mock_list):

        """Function:  test_mysql_80

        Description:  Test with MySQL 8.0 version database.

        Arguments:

        """

        mock_list.return_value = ["tbl1", "tbl2"]

        self.assertFalse(
            mysql_db_admin._proc_all_tbls(
                self.server, self.func_name, self.db_list, self.db_name,
                self.version2))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_pre_mysql_80(self, mock_list):

        """Function:  test_pre_mysql_80

        Description:  Test with pre MySQL 8.0 version database.

        Arguments:

        """

        mock_list.return_value = ["tbl1", "tbl2"]

        self.assertFalse(
            mysql_db_admin._proc_all_tbls(
                self.server, self.func_name, self.db_list, self.db_name,
                self.version))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    def test_no_tbls2(self):

        """Function:  test_no_tbls2

        Description:  Test with processing no tables.

        Arguments:

        """

        self.assertFalse(
            mysql_db_admin._proc_all_tbls(
                self.server, self.func_name, self.db_list, self.db_name4,
                self.version))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    def test_no_tbls(self):

        """Function:  test_no_tbls

        Description:  Test with processing no tables.

        Arguments:

        """

        self.assertFalse(
            mysql_db_admin._proc_all_tbls(
                self.server, self.func_name, self.db_list, self.db_name3,
                self.version))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_some_tbls(self, mock_list):

        """Function:  test_some_tbls

        Description:  Test with processing some tables.

        Arguments:

        """

        mock_list.return_value = ["tbl1", "tbl2"]

        self.assertFalse(
            mysql_db_admin._proc_all_tbls(
                self.server, self.func_name, self.db_list, self.db_name2,
                self.version))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_all_tbls(self, mock_list):

        """Function:  test_all_tbls

        Description:  Test with processing all tables.

        Arguments:

        """

        mock_list.return_value = ["tbl1", "tbl2"]

        self.assertFalse(
            mysql_db_admin._proc_all_tbls(
                self.server, self.func_name, self.db_list, self.db_name,
                self.version))


if __name__ == "__main__":
    unittest.main()
