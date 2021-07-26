"""# any test test file should have prefix as "test_"
# any code should be wrapped in methods
# test method name either should start with test_ or end with _test
# to run programs in terminal :
# navigate to pytest package (directory) then
# to run all tests in package : py.test
"""
import pytest


def test_d1_1():
    print("Hello")


@pytest.mark.xfail
def test_d1_2():
    msg = 'Sagar'
    assert msg == 'Hello'


def test_cross_browser(cross_browser):
    print(cross_browser[0])
    print(cross_browser[1])

