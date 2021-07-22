import pytest


@pytest.fixture()
def setup():
    print("Me first")
    yield
    print("Me showstoper")


def test_fixture_demo(setup):
    print("Me mandatory")
