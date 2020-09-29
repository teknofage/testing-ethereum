import pytest

@pytest.fixture(scope="module")
def token(Token, accounts):
    return Token.deploy("Test Token", "TST", 18, 10**21, {'from': accounts[0]})