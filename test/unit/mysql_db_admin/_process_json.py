#!/usr/bin/python
# Classification (U)

"""Program:  _process_json.py

    Description:  Unit testing of _process_json in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/_process_json.py

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
        __init__ -> Class initialization.
        add_2_msg -> add_2_msg method.
        send_mail -> send_mail method.

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
            (input) use_mailx -> True|False - To use mailx command.

        """

        _process_json = True

        if use_mailx:
            _process_json = True

        return _process_json


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_stdout -> Test with standard out.
        test_stdout_suppress_json -> Test with standard out being suppressed.
        test_mailx -> Test with using mailx.
        test_mail -> Test with emailing out.
        test_file -> Test with writing to file.
        test_append_to_file -> Test with appending to file.
        test_mongo_fail -> Test with failed mongo connection.
        test_mongo -> Test with mongo connection.
        test_non_json -> Test with in non-JSON format.
        test_json -> Test with in JSON format.
        test_flatten_json -> Test with flatten option for JSON format.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.args_array = {"-j": True, "-z": True}
        self.args_arraya = {"-j": True, "-z": True, "-u": True}
        self.args_array2 = {}
        self.args_array3 = {"-j": True}
        self.args_array4 = {"-j": True, "-a": True, "-z": True}
        self.args_array5 = {"-j": True, "-f": True, "-z": True}
        self.args_array6 = {"-z": True}
        self.args_array6a = {"-z": True, "-u": True}
        self.mode = "w"
        self.outdata = {"Application": "MySQL Database"}

    def test_stdout(self):

        """Function:  test_stdout

        Description:  Test with standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin._process_json(
                    self.args_array3, self.outdata, self.mode))

    def test_stdout_suppress_json(self):

        """Function:  test_stdout_suppress_json

        Description:  Test with standard out being suppressed.

        Arguments:

        """

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_array, self.outdata, self.mode))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mailx(self, mock_write, mock_mongo):

        """Function:  test_mailx

        Description:  Test with using mailx.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_arraya, self.outdata, self.mode, mail=self.mail))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mail(self, mock_write, mock_mongo):

        """Function:  test_mail

        Description:  Test with emailing out.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_array, self.outdata, self.mode, mail=self.mail))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_file(self, mock_write, mock_mongo):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_array, self.outdata, self.mode, ofile="FileName"))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_append_to_file(self, mock_write, mock_mongo):

        """Function:  test_append_to_file

        Description:  Test with appending to file.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_array4, self.outdata, self.mode, ofile="FileName"))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mongo_fail(self, mock_write, mock_mongo):

        """Function:  test_mongo_fail

        Description:  Test with mongo connection.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (False, "Error Message")

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin._process_json(
                    self.args_array, self.outdata, self.mode, class_cfg="Cfg",
                    db_tbl="db:tbl"))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mongo(self, mock_write, mock_mongo):

        """Function:  test_mongo

        Description:  Test with mongo connection.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_array, self.outdata, self.mode, class_cfg="Cfg",
                db_tbl="db:tbl"))

    def test_non_json(self):

        """Function:  test_non_json

        Description:  Test with in non-JSON format.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin._process_json(
                    self.args_array2, self.outdata, self.mode))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_json(self, mock_write, mock_mongo):

        """Function:  test_json

        Description:  Test with in JSON format.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_array, self.outdata, self.mode))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_flatten_json(self, mock_write, mock_mongo):

        """Function:  test_flatten_json

        Description:  Test with flatten option for JSON format.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args_array5, self.outdata, self.mode))


if __name__ == "__main__":
    unittest.main()
