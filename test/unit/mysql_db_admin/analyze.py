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

        self.args_array = {"-c": "mysql_cfg", "-d": "config", "-A": ["dbname"]}

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
        test_one_db_multiple_tbl
        test_one_db_one_tbl

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.db_tbl = {"db1": ["tbl1"]}
        self.db_tbl2 = {"db1": ["tbl1", "tbl2"]}
        self.db_tbl3 = {"db1": ["tbl1", "tbl2"], "db2": ["tbl3", "tbl4"]}
        self.template = {"Server": "ServerName"}
        self.config = {"config": "value"}
        self.analyze = [{"Status": "analyze", "Msg_text": "OK"}]

    @mock.patch("mysql_db_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.analyze_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_multiple_db_tbl(self, mock_dbdict, mock_template, mock_config,
                             mock_analyze):

        """Function:  test_multiple_db_tbl

        Description:  Test with multiple databases and multiple tables.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl3
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_analyze.return_value = self.analyze

        self.assertFalse(mysql_db_admin.analyze(self.server, self.args))

    @mock.patch("mysql_db_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.analyze_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_one_db_multiple_tbl(self, mock_dbdict, mock_template, mock_config,
                                 mock_analyze):

        """Function:  test_one_db_multiple_tbl

        Description:  Test with one database and multiple tables.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl2
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_analyze.return_value = self.analyze

        self.assertFalse(mysql_db_admin.analyze(self.server, self.args))

    @mock.patch("mysql_db_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("mysql_db_admin.mysql_libs.analyze_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_one_db_one_tbl(self, mock_dbdict, mock_template, mock_config,
                            mock_analyze):

        """Function:  test_one_db_one_tbl

        Description:  Test with one database and one table.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_analyze.return_value = self.analyze

        self.assertFalse(mysql_db_admin.analyze(self.server, self.args))


if __name__ == "__main__":
    unittest.main()
