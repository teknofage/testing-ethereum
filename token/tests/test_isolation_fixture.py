import pytest

@pytest.fixture(autouse=True)
def shared_setup(fn_isolation):
    pass