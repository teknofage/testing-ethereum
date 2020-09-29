import pytest
from brownie import accounts, Token


@pytest.fixture
def token():
    return Token.deploy("Test Token", "TST", 18, 10**21, {'from': accounts[0]})