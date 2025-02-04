# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/run_program.py

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
import mysql_db_admin                           # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def check(server, args, **kwargs):

    """Method:  check

    Description:  Function stub holder for mysql_db_admin.check.

    Arguments:
        (input) server > Stub holder
        (input) args -> Stub holder
        (input) **kwargs
            ofile -> Stub holder
            db_tbl -> Stub holder
            class_cfg -> Stub holder

    """

    ofile = kwargs.get("ofile", "file")
    status = True

    if server and args and ofile:
        status = True

    return status


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val
        get_args_keys

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config"}

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

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())


class Server():                                         # pylint:disable=R0903

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

        self.name = "Server_Name"
        self.conn_msg = None

    def connect(self, silent=False):

        """Method:  connect

        Description:  Stub method holder for mysql_class.Server.connect.

        Arguments:

        """

        status = True

        if silent:
            status = True

        return status


class Cfg():                                            # pylint:disable=R0903

    """Class:  Cfg

    Description:  Emulate a configuration file.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization.

        Arguments:

        """

        self.sys_dbs = [
            "performance_schema", "information_schema", "mysql", "sys"]


class Cfg2():                                           # pylint:disable=R0903

    """Class:  Cfg

    Description:  Emulate a configuration file.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization.

        Arguments:

        """

        self.sys_dbs2 = [
            "performance_schema", "information_schema", "mysql", "sys"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default_sys_dbs
        test_cfg_sys_dbs
        test_connect_failure
        test_connect_success
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.func_list = {"-C": check}

    @mock.patch("mysql_db_admin.gen_libs.load_module")
    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_default_sys_dbs(self, mock_inst, mock_disconn, mock_cfg):

        """Function:  test_default_sys_dbs

        Description:  Test default global sys_dbs variable.

        Arguments:

        """

        self.args.args_array["-C"] = True

        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_cfg.return_value = self.cfg2

        self.assertFalse(mysql_db_admin.run_program(self.args, self.func_list))

    @mock.patch("mysql_db_admin.gen_libs.load_module")
    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_cfg_sys_dbs(self, mock_inst, mock_disconn, mock_cfg):

        """Function:  test_cfg_sys_dbs

        Description:  Test configuration sys_dbs variable.

        Arguments:

        """

        self.args.args_array["-C"] = True

        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_db_admin.run_program(self.args, self.func_list))

    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_connect_failure(self, mock_inst, mock_disconn):

        """Function:  test_connect_failure

        Description:  Test with failed connection.

        Arguments:

        """

        self.server.conn_msg = "Error connection message"
        self.args.args_array["-C"] = True

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin.run_program(self.args, self.func_list))

    @mock.patch("mysql_db_admin.gen_libs.load_module")
    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_connect_success(self, mock_inst, mock_disconn, mock_cfg):

        """Function:  test_connect_success

        Description:  Test with successful connection.

        Arguments:

        """

        self.args.args_array["-C"] = True

        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_db_admin.run_program(self.args, self.func_list))

    @mock.patch("mysql_db_admin.gen_libs.load_module")
    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_run_program(self, mock_inst, mock_disconn, mock_cfg):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        self.args.args_array["-C"] = True

        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_db_admin.run_program(self.args, self.func_list))


if __name__ == "__main__":
    unittest.main()
