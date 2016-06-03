import unittest
from mock import MagicMock
from unittest_base_for_testing import MiddleManager, Employee, Executive, JuniorEmployee


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        """ call before every test case"""
        #class Report(object):
        #    MagicMock()
        Report = MagicMock()
        Report.append = MagicMock(return_value = "hello")


    def tearDown(self):
        """ call after every test case """

    def test_middlemanager_rank(self):
        mymiddlemanager = MiddleManager()
        assert mymiddlemanager.rank == 1

    def test_exec_report(self):
        from unittest_base_for_testing import Report
        """ composition example that assumes Report is already tested """
        """
            with
            patch()

        myexec = Executive()
        mock = MagicMock()
        myexec.write_report()
        myexec.write_report_item("hello")
        print myexec.get_report_items()
        """

    def test_exec_inherit_report(self):
        """ Dependency injection example, that mocks out report class """
        myexec = Executive()

        # mock out the report item
        mockreport = MagicMock()
        mockreport.add_item = MagicMock()
        mockreport.get_items = MagicMock(return_value = ["hello", "there"])

        myexec.inherit_report(mockreport)
        assert myexec.get_report_items() == ["hello", "there"]

