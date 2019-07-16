#!/usr/bin/python
# Classification (U)

"""Program:  optimize.py

    Description:  Unit testing of optimize in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/optimize.py

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

    Super-Class:

    Sub-Classes:

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_optimize -> Test optimize function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.run_optimize = True
        self.args_array = {"-D": True}

    @mock.patch("mysql_db_admin.process_request")
    def test_optimize(self, mock_process):

        """Function:  test_optimize

        Description:  Test optimize function.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_db_admin.optimize(self.server, self.args_array))


if __name__ == "__main__":
    unittest.main()
