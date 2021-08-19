#!/usr/bin/python
# Classification (U)

"""Program:  analyze.py

    Description:  Unit testing of analyze in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/analyze.py

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
        test_analyze

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.run_analyze = True
        self.args_array = {"-A": True}

    @mock.patch("mysql_db_admin.process_request")
    def test_analyze(self, mock_process):

        """Function:  test_analyze

        Description:  Test analyze function.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_db_admin.analyze(self.server, self.args_array))


if __name__ == "__main__":
    unittest.main()
