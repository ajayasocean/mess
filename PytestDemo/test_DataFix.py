import pytest


@pytest.mark.usefixtures("data_load")
class TestDataExample:

    def test_profile(self, data_load):
        print(data_load)
        print(data_load[0])
        print(data_load[2])
