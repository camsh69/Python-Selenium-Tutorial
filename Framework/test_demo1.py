import pytest
# Any pytest file shour start with _test or end with _test
# pytest method names should start with test
# Add the following to settings.json to enable pytest
#  "python.unitTest.pyTestEnabled": true,
#     "python.unitTest.unittestEnabled": false,
#     "python.unitTest.nosetestsEnabled": false
# Run on command line with 'pytest path_to_test_file.py' or 'pytest' to run all
# append -v : verbose, -q : quiet, -s : logs in output, -h : help,
# -k followed by string contained in methods to be run (e.g pytest -k Greeting -v -s)
# -m followed by (tag) mark (e.g. pytest -m smoke -v -s)
# skip test with @pytest.mark.skip
# run test but do not mark pass or fail with @pytest.mark.xfail


@pytest.mark.smoke
def test_firstProgram():
    print("hello")


def test_secondGreeting():
    msg = 'Hello'
    assert msg == 'Hello', 'Test failed because strings do not match'


@pytest.mark.skip
def test_thirdGreeting():
    msg = 'Hi'
    assert msg == 'Hello', 'Test failed because strings do not match'


@pytest.mark.xfail
def test_fourthGreeting():
    msg = 'Hello'
    assert msg == 'Hello', 'Test failed because strings do not match'
