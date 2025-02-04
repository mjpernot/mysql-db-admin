# Classification (U)

"""Program:  check.py

    Description:  Unit testing of check in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/check.py

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
import mysql_db_admin                           # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

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

        self.args_array = {"-c": "mysql_cfg", "-d": "config", "-C": ["dbname"]}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Server():                                         # pylint:disable=R0903

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multiline_return
        test_data_out_error
        test_multiple_db_tbl
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
        self.check = [{"Msg_type": "status", "Msg_text": "OK"}]
        self.check2 = [
            {"Msg_type": "status", "Msg_text": "OK"},
            {"Msg_type": "note", "Msg_text": "Message Here"}]

    @mock.patch("mysql_db_admin.data_out",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mysql_db_admin.mysql_libs.check_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_multiline_return(self, mock_dbdict, mock_template, mock_config,
                              mock_check):

        """Function:  test_multiline_return

        Description:  Test with analyze table returning multiple lines.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_check.return_value = self.check2

        self.assertFalse(mysql_db_admin.check(self.server, self.args))

    @mock.patch("mysql_db_admin.data_out",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mysql_db_admin.mysql_libs.check_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_data_out_error(self, mock_dbdict, mock_template, mock_config,
                            mock_check):

        """Function:  test_data_out_error

        Description:  Test with data_out return an error status.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl3
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_check.return_value = self.check

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.check(self.server, self.args))

    @mock.patch("mysql_db_admin.data_out",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mysql_db_admin.mysql_libs.check_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_multiple_db_tbl(self, mock_dbdict, mock_template, mock_config,
                             mock_check):

        """Function:  test_multiple_db_tbl

        Description:  Test with multiple databases and multiple tables.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl3
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_check.return_value = self.check

        self.assertFalse(mysql_db_admin.check(self.server, self.args))

    @mock.patch("mysql_db_admin.data_out",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mysql_db_admin.mysql_libs.check_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_one_db_multiple_tbl(self, mock_dbdict, mock_template, mock_config,
                                 mock_check):

        """Function:  test_one_db_multiple_tbl

        Description:  Test with one database and multiple tables.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl2
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_check.return_value = self.check

        self.assertFalse(mysql_db_admin.check(self.server, self.args))

    @mock.patch("mysql_db_admin.data_out",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mysql_db_admin.mysql_libs.check_tbl")
    @mock.patch("mysql_db_admin.create_data_config")
    @mock.patch("mysql_db_admin.get_json_template")
    @mock.patch("mysql_db_admin.get_db_tbl")
    def test_one_db_one_tbl(self, mock_dbdict, mock_template, mock_config,
                            mock_check):

        """Function:  test_one_db_one_tbl

        Description:  Test with one database and one table.

        Arguments:

        """

        mock_dbdict.return_value = self.db_tbl
        mock_template.return_value = self.template
        mock_config.return_value = self.config
        mock_check.return_value = self.check

        self.assertFalse(mysql_db_admin.check(self.server, self.args))


if __name__ == "__main__":
    unittest.main()
