# fixture is declared in conftest.py as to use it as common method
# to run the test : py.test test_FixtureDemo.py -q -v -s
import pytest


@pytest.mark.usefixtures("setup")
class TestFix:
    def test_fixture_demo1(self):
        print("Me mandatory")

    def test_fixture_demo2(self):
        print("Me Urgent")
