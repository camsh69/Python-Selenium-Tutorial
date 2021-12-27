import pytest
# see conftest file
# fixtures are used for setup and tear down for test cases - conftest file to generalize and make fixture available in all files


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("I will execute as part of fixtureDemo")

    def test_fixtureDemo1(self):
        print("I will execute as part of fixtureDemo")

    def test_fixtureDemo2(self):
        print("I will execute as part of fixtureDemo")

    def test_fixtureDemo3(self):
        print("I will execute as part of fixtureDemo")
