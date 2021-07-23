import pytest


@pytest.fixture(scope='class')
def setup():
    print("Me first")
    yield
    print("Me showstopper")
