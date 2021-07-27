"""# any test test file should have prefix as "test_"
# any code should be wrapped in methods
# test method name either should start with test_ or end with _test
# to run programs in terminal :
# navigate to pytest package (directory) then
# to run all tests in package : py.test
to run:  py.test test_d1.py --html=report.html
"""

import pytest
from PytestDemo.LogClass import LogClass

class TestD1(LogClass):

    def test_d1_1(self):
        log = self.get_logger()
        log.info("Hello")
        # print("Hello")

    @pytest.mark.xfail
    def test_d1_2(self):
        msg = 'Sagar'
        assert msg == 'Hello'
        log = self.get_logger()
        log.info("msg = 'Sagar'")

    def test_cross_browser(self, cross_browser):
        log = self.get_logger()
        log.debug(cross_browser[0])
        log.debug(cross_browser[1])
        # print(cross_browser[0])
        # print(cross_browser[1])
