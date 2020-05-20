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
import version

__version__ = version.__version__


def check(server, args_array, **kwargs):

    """Method:  check

    Description:  Function stub holder for mysql_db_admin.check.

    Arguments:
        (input) server -> Server instance.
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
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mysql_class.Server.connect.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_email -> Test with email option.
        test_mongo -> Test with mongo option.
        test_run_program -> Test run_program function.

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

    @mock.patch("mysql_db_admin.cmds_gen.disconnect")
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

    @mock.patch("mysql_db_admin.cmds_gen.disconnect")
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

    @mock.patch("mysql_db_admin.cmds_gen.disconnect")
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
