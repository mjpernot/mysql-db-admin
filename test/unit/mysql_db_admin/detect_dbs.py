#!/usr/bin/python
# Classification (U)

"""Program:  detect_dbs.py

    Description:  Unit testing of detect_dbs in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/detect_dbs.py

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

# Local
sys.path.append(os.getcwd())
import mysql_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_miss_db
        test_miss_db

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.db1a = ["db1", "db2", "db3", "db4"]
        self.db1b = ["db1", "db2", "db3"]
        self.db2 = ["db1", "db2", "db3"]

    def test_no_miss_db(self):

        """Function:  test_no_miss_db

        Description:  Test with no missing databases.

        Arguments:

        """

        self.assertFalse(mysql_db_admin.detect_dbs(self.db1b, self.db2))

    def test_miss_db(self):

        """Function:  test_miss_db

        Description:  Test with missing database.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.detect_dbs(self.db1a, self.db2))


if __name__ == "__main__":
    unittest.main()
