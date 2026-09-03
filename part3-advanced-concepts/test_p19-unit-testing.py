import pytest

@pytest.fixture
def db_connection():
    print("Setup")
    yield "Connected"
    print("Cleaup/Teardown")


def test_db(db_connection):
    assert db_connection=="Connected"

def test_sum(sample_data):
    assert sum(sample_data)==6