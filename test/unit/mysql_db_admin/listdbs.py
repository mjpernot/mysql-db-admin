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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config", "-L": True}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False


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
        test_all_dbs
        test_user_dbs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
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

        self.args.args_array["-k"] = True

        mock_list.return_value = self.db_list

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin.listdbs(
                    self.server, self.args, sys_dbs=self.sys_dbs))

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
                    self.server, self.args, sys_dbs=self.sys_dbs))


if __name__ == "__main__":
    unittest.main()
