
import pytest

@pytest.mark.parametrize("amount", [0, 31337, 10**18])
def test_transfer_adjusts_receiver_balance(accounts, token, amount):
    balance = token.balanceOf(accounts[1])
    token.transfer(accounts[1], amount, {'from': accounts[0]})
    
    assert token.balanceOf(accounts[1]) == balance + amount