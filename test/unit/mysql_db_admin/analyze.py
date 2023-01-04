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

import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_admin
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config"}

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
        test_db_tbl
        test_db_only

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args.args_array["-A"] = ["db_name"]
        self.run_analyze = True

    @mock.patch("mysql_db_admin.process_request")
    def test_db_tbl(self, mock_process):

        """Function:  test_db_tbl

        Description:  Test check function with database and table names.

        Arguments:

        """

        self.args.args_array["-t"] = ["tbl_name"]

        mock_process.return_value = True

        self.assertFalse(mysql_db_admin.analyze(self.server, self.args))

    @mock.patch("mysql_db_admin.process_request")
    def test_db_only(self, mock_process):

        """Function:  test_db_only

        Description:  Test check function with database name only.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_db_admin.analyze(self.server, self.args))


if __name__ == "__main__":
    unittest.main()
