# Classification (U)

"""Program:  get_db_tbl.py

    Description:  Unit testing of get_db_tbl in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/get_db_tbl.py

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
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config", "-A": ["dbname"]}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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

        self.version = (8, 0)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_one_db_multiple_tbl
        test_one_db_one_tbl

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.db_list = list()
        self.db_list2 = ["db1"]
        self.db_list3 = ["systemdb"]
        self.db_list4 = ["systemdb", "db1"]
        self.db_list5 = ["db1", "db2"]
        self.tbl_list = ["tbl1"]
        self.tbl_list2 = ["tbl1", "tbl2"]
        self.tbl_dict = [{"TABLE_NAME": "t2"}]
        self.tbl_dict2 = [{"TABLE_NAME": "t1"}, {"TABLE_NAME": "t2"}]
        self.tbl_dict = [{"table_name": "t2"}]
        self.tbl_dict2 = [{"table_name": "t1"}, {"table_name": "t2"}]
        self.system_dbs = list()
        self.system_dbs2 = ["systemdb"]

    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    def test_pre_80(self, mock_fetch):

        """Function:  test_pre_80

        Description:  Test with pre MySQL 8.0 version.

        Arguments:

        """

        mock_fetch.return_value = self.tbl_dict

        self.assertEqual(
            mysql_db_admin.get_all_dbs_tbls(
                self.server, self.db_list, self.dict_key), self.results)


if __name__ == "__main__":
    unittest.main()
