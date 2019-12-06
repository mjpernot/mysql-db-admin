#!/usr/bin/python
# Classification (U)

"""Program:  run_optimize.py

    Description:  Unit testing of run_optimize in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/run_optimize.py

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
        test_run_optimize -> Test run_optimize function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

        self.optimize_tbl = \
            [{"Msg_type": "note",
              "Msg_text": "Table does not support optimize, doing recreate + \
analyze instead"},
             {"Msg_type": "Type2", "Msg_text": "Message2"}]

    @mock.patch("mysql_db_admin.gen_libs.prt_msg")
    @mock.patch("mysql_db_admin.mysql_libs.optimize_tbl")
    def test_run_optimize(self, mock_optimize, mock_prt):

        """Function:  test_run_optimize

        Description:  Test run_optimize function.

        Arguments:

        """

        mock_optimize.return_value = self.optimize_tbl
        mock_prt.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.run_optimize(self.server, "db",
                                                         "tbl"))


if __name__ == "__main__":
    unittest.main()
