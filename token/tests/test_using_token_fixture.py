def test_transfer_adjusts_sender_balance(token):
    balance = token.balanceOf(accounts[0])
    token.transfer(accounts[1], 10**18, {'from': accounts[0]})
    
    assert token.balanceOf(accounts[0]) == balance - 10**18
 

def test_transfer_adjusts_receiver_balance(token):
    balance = token.balanceOf(accounts[1])
    token.transfer(accounts[1], 10**18, {'from': accounts[0]})
    
    assert token.balanceOf(accounts[1]) == balance + 10**18
  

def test_transfer_fails_from_insufficient_balance(token):
    with brownie.reverts("Insufficient Balance"):
        token.transfer(accounts[2], 10**18, {'from': accounts[1]})