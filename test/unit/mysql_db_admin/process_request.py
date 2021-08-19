#!/usr/bin/python
# Classification (U)

"""Program:  process_request.py

    Description:  Unit testing of process_request in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/process_request.py

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
        test_single_miss_tbl
        test_single_tbl
        test_all_tbls
        test_all_dbs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.func_name = func_holder
        self.db_name = None
        self.db_name2 = ["db1"]
        self.tbl_name = None
        self.tbl_name2 = ["tbl1"]
        self.tbl_name3 = ["tbl3"]
        self.version = {"version": "5.7"}
        self.version2 = {"version": "8.0"}

    @mock.patch("mysql_db_admin.mysql_class.fetch_sys_var")
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict")
    def test_mysql_80(self, mock_fetch_db, mock_fetch_tbl, mock_list,
                      mock_version):

        """Function:  test_mysql_80

        Description:  Test with processing all databases.

        Arguments:

        """

        mock_version.return_value = self.version2
        mock_fetch_db.return_value = True
        mock_fetch_tbl.return_value = True
        mock_list.side_effect = [["db1"], ["tbl1", "tbl2"]]

        self.assertFalse(
            mysql_db_admin.process_request(
                self.server, self.func_name, self.db_name, self.tbl_name))

    @mock.patch("mysql_db_admin.mysql_class.fetch_sys_var")
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict")
    def test_pre_mysql_80(self, mock_fetch_db, mock_fetch_tbl, mock_list,
                          mock_version):

        """Function:  test_pre_mysql_80

        Description:  Test with processing all databases.

        Arguments:

        """

        mock_version.return_value = self.version
        mock_fetch_db.return_value = True
        mock_fetch_tbl.return_value = True
        mock_list.side_effect = [["db1"], ["tbl1", "tbl2"]]

        self.assertFalse(
            mysql_db_admin.process_request(
                self.server, self.func_name, self.db_name, self.tbl_name))

    @mock.patch("mysql_db_admin.mysql_class.fetch_sys_var")
    @mock.patch("mysql_db_admin.detect_dbs")
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict")
    def test_single_miss_tbl(self, mock_fetch_db, mock_fetch_tbl, mock_list,
                             mock_detect, mock_version):

        """Function:  test_single_miss_tbl

        Description:  Test with single missing table in a database.

        Arguments:

        """

        mock_version.return_value = self.version
        mock_fetch_db.return_value = True
        mock_fetch_tbl.return_value = True
        mock_list.side_effect = [["db1"], ["tbl1", "tbl2"]]
        mock_detect.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin.process_request(
                    self.server, self.func_name, self.db_name2,
                    self.tbl_name3))

    @mock.patch("mysql_db_admin.mysql_class.fetch_sys_var")
    @mock.patch("mysql_db_admin.detect_dbs")
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict")
    def test_single_tbl(self, mock_fetch_db, mock_fetch_tbl, mock_list,
                        mock_detect, mock_version):

        """Function:  test_single_tbl

        Description:  Test with single table in a database.

        Arguments:

        """

        mock_version.return_value = self.version
        mock_fetch_db.return_value = True
        mock_fetch_tbl.return_value = True
        mock_list.side_effect = [["db1"], ["tbl1", "tbl2"]]
        mock_detect.return_value = True

        self.assertFalse(
            mysql_db_admin.process_request(
                self.server, self.func_name, self.db_name2, self.tbl_name2))

    @mock.patch("mysql_db_admin.mysql_class.fetch_sys_var")
    @mock.patch("mysql_db_admin.detect_dbs")
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict")
    def test_all_tbls(self, mock_fetch_db, mock_fetch_tbl, mock_list,
                      mock_detect, mock_version):

        """Function:  test_all_tbls

        Description:  Test with all tables in a database.

        Arguments:

        """

        mock_version.return_value = self.version
        mock_fetch_db.return_value = True
        mock_fetch_tbl.return_value = True
        mock_list.side_effect = [["db1"], ["tbl1", "tbl2"]]
        mock_detect.return_value = True

        self.assertFalse(
            mysql_db_admin.process_request(
                self.server, self.func_name, self.db_name2, self.tbl_name))

    @mock.patch("mysql_db_admin.mysql_class.fetch_sys_var")
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict")
    def test_all_dbs(self, mock_fetch_db, mock_fetch_tbl, mock_list,
                     mock_version):

        """Function:  test_all_dbs

        Description:  Test with processing all databases.

        Arguments:

        """

        mock_version.return_value = self.version
        mock_fetch_db.return_value = True
        mock_fetch_tbl.return_value = True
        mock_list.side_effect = [["db1"], ["tbl1", "tbl2"]]

        self.assertFalse(
            mysql_db_admin.process_request(
                self.server, self.func_name, self.db_name, self.tbl_name))


if __name__ == "__main__":
    unittest.main()
