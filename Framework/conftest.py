import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile is being created")
    return ['Campbell', 'Forsyth', 'campbellforsyth.com']


@pytest.fixture(params=[("chrome", "Campbell"), "Firefox", "Edge"])
def crossBrowser(request):
    return request.param
