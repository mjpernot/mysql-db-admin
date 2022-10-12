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

        _process_json = True

        if use_mailx:
            _process_json = True

        return _process_json


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_stdout
        test_stdout_suppress_json
        test_mailx
        test_mail
        test_file
        test_append_to_file
        test_mongo_fail
        test_mongo
        test_non_json
        test_json
        test_flatten_json

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.args = ArgParser()
        self.mode = "w"
        self.outdata = {"Application": "MySQL Database"}

    def test_stdout(self):

        """Function:  test_stdout

        Description:  Test with standard out.

        Arguments:

        """

        self.args.args_array["-j"] = True

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin._process_json(
                    self.args, self.outdata, self.mode))

    def test_stdout_suppress_json(self):

        """Function:  test_stdout_suppress_json

        Description:  Test with standard out being suppressed.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True

        self.assertFalse(
            mysql_db_admin._process_json(self.args, self.outdata, self.mode))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mailx(self, mock_write, mock_mongo):

        """Function:  test_mailx

        Description:  Test with using mailx.

        Arguments:

        """

        self.args.args_array["-u"] = True
        self.args.args_array["-z"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args, self.outdata, self.mode, mail=self.mail))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mail(self, mock_write, mock_mongo):

        """Function:  test_mail

        Description:  Test with emailing out.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args, self.outdata, self.mode, mail=self.mail))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_file(self, mock_write, mock_mongo):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args, self.outdata, self.mode, ofile="FileName"))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_append_to_file(self, mock_write, mock_mongo):

        """Function:  test_append_to_file

        Description:  Test with appending to file.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True
        self.args.args_array["-a"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args, self.outdata, self.mode, ofile="FileName"))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mongo_fail(self, mock_write, mock_mongo):

        """Function:  test_mongo_fail

        Description:  Test with mongo connection.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (False, "Error Message")

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin._process_json(
                    self.args, self.outdata, self.mode, class_cfg="Cfg",
                    db_tbl="db:tbl"))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mongo(self, mock_write, mock_mongo):

        """Function:  test_mongo

        Description:  Test with mongo connection.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args, self.outdata, self.mode, class_cfg="Cfg",
                db_tbl="db:tbl"))

    def test_non_json(self):

        """Function:  test_non_json

        Description:  Test with in non-JSON format.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_db_admin._process_json(
                    self.args, self.outdata, self.mode))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_json(self, mock_write, mock_mongo):

        """Function:  test_json

        Description:  Test with in JSON format.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(self.args, self.outdata, self.mode))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_flatten_json(self, mock_write, mock_mongo):

        """Function:  test_flatten_json

        Description:  Test with flatten option for JSON format.

        Arguments:

        """

        self.args.args_array["-j"] = True
        self.args.args_array["-z"] = True
        self.args.args_array["-f"] = True

        mock_write.return_value = True
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_db_admin._process_json(
                self.args, self.outdata, self.mode))


if __name__ == "__main__":
    unittest.main()
