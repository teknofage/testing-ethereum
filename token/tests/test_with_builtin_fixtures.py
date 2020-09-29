import brownie
import pytest

@pytest.fixture
def token(Token, accounts):
    return Token.deploy("Test Token", "TST", 18, 10**21, {'from': accounts[0]})


def test_transfer_adjusts_sender_balance(accounts, token):
    balance = token.balanceOf(accounts[0])
    token.transfer(accounts[1], 10**18, {'from': accounts[0]})
    
    assert token.balanceOf(accounts[0]) == balance - 10**18
 

def test_transfer_adjusts_receiver_balance(accounts, token):
    balance = token.balanceOf(accounts[1])
    token.transfer(accounts[1], 10**18, {'from': accounts[0]})
    
    assert token.balanceOf(accounts[1]) == balance + 10**18

    
def test_transfer_fails_from_insufficient_balance(accounts, token):
    with brownie.reverts("Insufficient Balance"):
        token.transfer(accounts[2], 10**18, {'from': accounts[1]})