#!/usr/bin/python
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


def check(server, args_array, **kwargs):

    """Method:  check

    Description:  Function stub holder for mysql_db_admin.check.

    Arguments:
        (input) server
        (input) args_array -> Stub holder
        (input) **kwargs
            ofile -> Stub holder
            db_tbl -> Stub holder
            class_cfg -> Stub holder

    """

    ofile = kwargs.get("ofile", "file")
    status = True

    if server and args_array and ofile:
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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_connect_failure
        test_connect_success
        test_email
        test_mongo
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.func_dict = {"-C": check}
        self.args_array = {"-m": True, "-d": True, "-c": True, "-C": True}
        self.args_array2 = {"-m": True, "-d": True, "-c": True, "-C": True,
                            "-e": "ToEmail", "-s": "SubjectLine"}
        self.args_array3 = {"-d": True, "-c": True, "-C": True}

    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_connect_failure(self, mock_inst, mock_disconn):

        """Function:  test_connect_failure

        Description:  Test with failed connection.

        Arguments:

        """

        self.server.conn_msg = "Error connection message"

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.run_program(self.args_array3,
                                                        self.func_dict))

    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_connect_success(self, mock_inst, mock_disconn):

        """Function:  test_connect_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mysql_db_admin.run_program(self.args_array3,
                                                    self.func_dict))

    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.gen_libs.load_module")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_email(self, mock_inst, mock_mongo, mock_disconn):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_mongo.return_value = True
        mock_disconn.return_value = True

        self.assertFalse(mysql_db_admin.run_program(self.args_array2,
                                                    self.func_dict))

    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.gen_libs.load_module")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_mongo(self, mock_inst, mock_mongo, mock_disconn):

        """Function:  test_mongo

        Description:  Test with mongo option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_mongo.return_value = True
        mock_disconn.return_value = True

        self.assertFalse(mysql_db_admin.run_program(self.args_array,
                                                    self.func_dict))

    @mock.patch("mysql_db_admin.mysql_libs.disconnect")
    @mock.patch("mysql_db_admin.mysql_libs.create_instance")
    def test_run_program(self, mock_inst, mock_disconn):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mysql_db_admin.run_program(self.args_array3,
                                                    self.func_dict))


if __name__ == "__main__":
    unittest.main()
