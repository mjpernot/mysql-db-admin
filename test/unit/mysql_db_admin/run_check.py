# Classification (U)

"""Program:  run_check.py

    Description:  Unit testing of run_check in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/run_check.py

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
        test_run_check

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

        self.check_tbl = [{"Msg_type": "Type", "Msg_text": "Message"},
                          {"Msg_type": "Type2", "Msg_text": "Message2"}]

    @mock.patch("mysql_db_admin.gen_libs.prt_msg")
    @mock.patch("mysql_db_admin.mysql_libs.check_tbl")
    def test_run_check(self, mock_check, mock_prt):

        """Function:  test_run_check

        Description:  Test run_check function.

        Arguments:

        """

        mock_check.return_value = self.check_tbl
        mock_prt.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.run_check(self.server, "db",
                                                      "tbl"))


if __name__ == "__main__":
    unittest.main()
