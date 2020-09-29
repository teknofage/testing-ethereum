def test_transfer_adjusts_receiver_balance(accounts, token):
    balance = token.balanceOf(accounts[1])
    token.transfer(accounts[1], 10**18, {'from': accounts[0]})
    
    assert token.balanceOf(accounts[1]) == balance + 10**18