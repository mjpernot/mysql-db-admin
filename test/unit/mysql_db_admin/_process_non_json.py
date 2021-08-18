#!/usr/bin/python
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
        self.args_array = {"-z": True}
        self.args_arraya = {"-z": True, "-u": True}
        self.args_array2 = {}
        self.mode = "w"
        self.outdata = {"Application": "MySQL Database"}

    def test_mailx_non_json(self):

        """Function:  test_mailx_non_json

        Description:  Test with using mailx.

        Arguments:

        """

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args_arraya, self.outdata, self.mode,
            mail=self.mail))

    def test_mail_non_json(self):

        """Function:  test_mail_non_json

        Description:  Test with emailing out.

        Arguments:

        """

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args_array, self.outdata, self.mode,
            mail=self.mail))

    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_file_non_json(self, mock_write):

        """Function:  test_file_non_json

        Description:  Test with writing to file for standard format.

        Arguments:

        """

        mock_write.return_value = True

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args_array, self.outdata, self.mode,
            ofile="FileName"))

    def test_stdout_suppress_non_json(self):

        """Function:  test_stdout_suppress_non_json

        Description:  Test with standard out being suppressed.

        Arguments:

        """

        self.assertFalse(mysql_db_admin._process_non_json(
            self.server, self.args_array, self.outdata, self.mode))

    def test_non_json(self):

        """Function:  test_non_json

        Description:  Test with in non-JSON format.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin._process_non_json(
                self.server, self.args_array2, self.outdata, self.mode))


if __name__ == "__main__":
    unittest.main()
