#!/usr/bin/python
# Classification (U)

"""Program:  run_checksum.py

    Description:  Unit testing of run_checksum in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/run_checksum.py

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
        test_run_checksum -> Test run_checksum function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

        self.checksum = [{"Checksum": "Sum"}]

    @mock.patch("mysql_db_admin.mysql_libs.checksum")
    def test_run_checksum(self, mock_checksum):

        """Function:  test_run_checksum

        Description:  Test run_checksum function.

        Arguments:

        """

        mock_checksum.return_value = self.checksum

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.run_checksum(self.server, "db",
                                                         "tbl"))


if __name__ == "__main__":
    unittest.main()
