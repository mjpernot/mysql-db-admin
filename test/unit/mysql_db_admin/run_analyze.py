#!/usr/bin/python
# Classification (U)

"""Program:  run_analyze.py

    Description:  Unit testing of run_analyze in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/run_analyze.py

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
        test_run_analyze

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

        self.analyze_tables = [{"Msg_type": "Type", "Msg_text": "Message"},
                               {"Msg_type": "Type2", "Msg_text": "Message2"}]

    @mock.patch("mysql_db_admin.gen_libs.prt_msg")
    @mock.patch("mysql_db_admin.mysql_libs.analyze_tbl")
    def test_run_analyze(self, mock_analyze, mock_prt):

        """Function:  test_run_analyze

        Description:  Test run_analyze function.

        Arguments:

        """

        mock_analyze.return_value = self.analyze_tables
        mock_prt.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.run_analyze(self.server, "db",
                                                        "tbl"))


if __name__ == "__main__":
    unittest.main()
