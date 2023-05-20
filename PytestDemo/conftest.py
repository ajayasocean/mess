import pytest


@pytest.fixture(scope='class')
def setup():
    print("Me first")

    print("Me showstopper")


@pytest.fixture()
def data_load():
    print("Creating required data")
    return ["Ajay", "Sagar", "SDET"]


@pytest.fixture(params=[('chrome', 'Ajay'), ('firefox', 'Sagar')])
def cross_browser(request):
    return request.param

