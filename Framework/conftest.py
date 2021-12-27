import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile is being created")
    return ('Campbell', 'Forsyth', 'campbellforsyth.com')
