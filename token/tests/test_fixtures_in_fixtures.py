import pytest
from brownie import accounts, Token


@pytest.fixture
def token():
    return Token.deploy("Test Token", "TST", 18, 10**21, {'from': accounts[0]})

  
@pytest.fixture
def distribute_tokens(token):
    for i in range(1, 10):
        token.transfer(accounts[i], 100, {'from': accounts[0]})