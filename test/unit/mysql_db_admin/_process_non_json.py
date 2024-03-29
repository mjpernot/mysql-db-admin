# Classification (U)

"""Program:  _process_non_json.py

    Description:  Unit testing of _process_non_json in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/_process_non_json.py

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


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config"}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self, lag_time=1):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.lag_time = lag_time
        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.data = data

        return True

    def send_mail(self, use_mailx=False):

        """Method:  get_name

        Description:  Stub method holder for Mail.send_mail.

        Arguments:
            (input) use_mailx

        """

        status = True

        if use_mailx:
            status = True

        return status


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__
        upd_srv_stat

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.cur_mem_mb = "cur_mem_mb"
        self.max_mem_mb = "max_mem_mb"
        self.prct_mem = "prct_mem"
        self.days_up = "days_up"
        self.cur_conn = "cur_conn"
        self.max_conn = "max_conn"
        self.prct_conn = "prct_conn"

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Stub method holder for mysql_class.Server.upd_srv_stat.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mailx_non_json
        test_mail_non_json
        test_file_non_json
        test_stdout_suppress_non_json
        test_non_json

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.args = ArgParser()
        self.mode = "w"
        self.outdata = {"Application": "MySQL Database"}

    def test_mailx_non_json(self):

        """Function:  test_mailx_non_json

        Description:  Test with using mailx.

        Arguments:

        """

        self.args.args_array["-z"] = True
        self.args.args_array["-u"] = True

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args, self.outdata, self.mode, mail=self.mail))

    def test_mail_non_json(self):

        """Function:  test_mail_non_json

        Description:  Test with emailing out.

        Arguments:

        """

        self.args.args_array["-z"] = True

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args, self.outdata, self.mode, mail=self.mail))

    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_file_non_json(self, mock_write):

        """Function:  test_file_non_json

        Description:  Test with writing to file for standard format.

        Arguments:

        """

        self.args.args_array["-z"] = True

        mock_write.return_value = True

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args, self.outdata, self.mode, ofile="FileName"))

    def test_stdout_suppress_non_json(self):

        """Function:  test_stdout_suppress_non_json

        Description:  Test with standard out being suppressed.

        Arguments:

        """

        self.args.args_array["-z"] = True

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args, self.outdata, self.mode))

    def test_non_json(self):

        """Function:  test_non_json

        Description:  Test with in non-JSON format.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin._process_non_json(
                self.server, self.args, self.outdata, self.mode))


if __name__ == "__main__":
    unittest.main()
