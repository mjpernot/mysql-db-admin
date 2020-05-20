#!/usr/bin/python
# Classification (U)

"""Program:  proc_some_tbls.py

    Description:  Unit testing of _proc_some_tbls in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/proc_some_tbls.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def func_holder(server, dbs, tbl):

    """Method:  func_holder

    Description:  Function stub holder for a generic function call.

    Arguments:
        server -> Server class instance.
        dbs -> Database name.
        tbl -> Table name.

    """

    status = True

    if server and dbs and tbl:
        status = True

    return status


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__ -> Class initialization.

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
        setUp -> Initialize testing environment.
        test_miss_dbs -> Test with processing missing database.
        test_no_dbs -> Test with processing no databases.
        test_miss_tbls -> Test with processing missing tables.
        test_no_tbls -> Test with processing no tables.
        test_some_tbls -> Test with processing some tables.
        test_all_tbls -> Test with processing all tables.

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
        self.tbl_name = ["tbl1", "tbl2"]
        self.tbl_name2 = ["tbl1"]
        self.tbl_name3 = []
        self.tbl_name4 = ["tbl1", "tbl3"]

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    def test_miss_dbs(self):

        """Function:  test_miss_dbs

        Description:  Test with processing missing database.

        Arguments:

        """

        self.assertFalse(mysql_db_admin._proc_some_tbls(
            self.server, self.func_name, self.db_list, self.db_name4,
            self.tbl_name4))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    def test_no_dbs(self):

        """Function:  test_no_dbs

        Description:  Test with processing no databases.

        Arguments:

        """

        self.assertFalse(mysql_db_admin._proc_some_tbls(
            self.server, self.func_name, self.db_list, self.db_name3,
            self.tbl_name4))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_miss_tbls(self, mock_list):

        """Function:  test_miss_tbls

        Description:  Test with processing missing tables.

        Arguments:

        """

        mock_list.return_value = ["tbl1", "tbl2"]

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin._proc_some_tbls(
                self.server, self.func_name, self.db_list, self.db_name2,
                self.tbl_name4))

    @mock.patch("mysql_db_admin.detect_dbs", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_no_tbls(self, mock_list):

        """Function:  test_no_tbls

        Description:  Test with processing no tables.

        Arguments:

        """

        mock_list.return_value = ["tbl1", "tbl2"]

        self.assertFalse(mysql_db_admin._proc_some_tbls(
            self.server, self.func_name, self.db_list, self.db_name2,
            self.tbl_name3))

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

        self.assertFalse(mysql_db_admin._proc_some_tbls(
            self.server, self.func_name, self.db_list, self.db_name2,
            self.tbl_name2))

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

        self.assertFalse(mysql_db_admin._proc_some_tbls(
            self.server, self.func_name, self.db_list, self.db_name,
            self.tbl_name))


if __name__ == "__main__":
    unittest.main()
