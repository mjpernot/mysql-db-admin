# Classification (U)

"""Program:  status.py

    Description:  Unit testing of status in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/status.py

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

        self.args_array = {"-c": "mysql_cfg", "-d": "config", "-S": True}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False

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
        upd_srv_stat

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.cur_mem_mb = "cur_mem_mb"
        self.max_mem_mb = "max_mem_mb"
        self.prct_mem = "prct_mem"
        self.days_up = "days_up"
        self.cur_conn = "cur_conn"
        self.max_conn = "max_conn"
        self.prct_conn = "prct_conn"

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Stub method holder for mysql_class.Server.upd_srv_stat.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_data_out_error
        test_status

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()

    @mock.patch("mysql_db_admin.data_out",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    def test_data_out_error(self, mock_template, mock_config):

        """Function:  test_data_out_error

        Description:  Test with data_out return an error status.

        Arguments:

        """

        mock_template.return_value = self.template
        mock_config.return_value = self.config

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.checksum(self.server, self.args))

    @mock.patch("mysql_db_admin.data_out",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    def test_status(self, mock_template, mock_config):

        """Function:  test_status

        Description:  Test status function.

        Arguments:

        """

        mock_template.return_value = self.template
        mock_config.return_value = self.config

        self.assertFalse(mysql_db_admin.checksum(self.server, self.args))


if __name__ == "__main__":
    unittest.main()
