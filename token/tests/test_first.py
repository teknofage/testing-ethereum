from brownie import accounts, Token

def test_transfer_adjusts_sender_balance():
    token = Token.deploy("Test Token", "TST", 18, 10**21, {'from': accounts[0]})
    balance = token.balanceOf(accounts[0])
    
    token.transfer(accounts[1], 10**18, {'from': accounts[0]})
    
    assert token.balanceOf(accounts[0]) == balance - 10**18