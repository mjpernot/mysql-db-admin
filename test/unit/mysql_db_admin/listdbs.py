#!/usr/bin/python
# Classification (U)

"""Program:  listdbs.py

    Description:  Unit testing of listdbs in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/listdbs.py

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
        test_all_dbs -> Test with listing all databases.
        test_user_dbs -> Test with listing only user databases.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-L": True}
        self.args_array2 = {"-L": True, "-k": True}
        self.db_list = ["db1", "db2", "performance_schema",
                        "information_schema", "mysql", "sys"]
        self.sys_dbs = ["performance_schema", "information_schema", "mysql",
                        "sys"]

    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_all_dbs(self, mock_list):

        """Function:  test_all_dbs

        Description:  Test with listing all databases.

        Arguments:

        """

        mock_list.return_value = self.db_list

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin.listdbs(
                    self.server, self.args_array2, sys_dbs=self.sys_dbs))

    @mock.patch("mysql_db_admin.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    def test_user_dbs(self, mock_list):

        """Function:  test_user_dbs

        Description:  Test with listing only user databases.

        Arguments:

        """

        mock_list.return_value = self.db_list

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin.listdbs(
                    self.server, self.args_array, sys_dbs=self.sys_dbs))


if __name__ == "__main__":
    unittest.main()
