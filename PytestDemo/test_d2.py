"""# any test test file should have prefix as "test_"
# any code should be wrapped in methods

# test method name either should start with test_ or end with _test
# to run programs in terminal :
# navigate to pytest package (directory) then
# to run all tests in package : py.test
# to run all tests in package with details : py.test -v -s
"""


def test_3():
    msg = 'Hello'
    assert msg == 'Hello'


