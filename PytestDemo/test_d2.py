"""# any test test file should have prefix as "test_"
# any code should be wrapped in methods

# test method name either should start with test_ or end with _test
# to run programs in terminal :
# navigate to pytest package (directory) then
# to run all tests in package : py.test
# to run all tests in package with details : py.test -v -s
"""
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_d2_1():
    msg = 'Welcome'
    assert msg == 'Sagar'


def test_d2_2():
    a = 4
    b = 6
    assert a+2 == b, "Additon match"



