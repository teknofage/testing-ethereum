import brownie
from brownie import accounts, Token

def test_transfer_fails_from_insufficient_balance():
    token = Token.deploy("Test Token", "TST", 18, 10**21, {'from': accounts[0]})
   
    with brownie.reverts("Insufficient balance"):
        token.transfer(accounts[2], 10**18, {'from': accounts[1]})