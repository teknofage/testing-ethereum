
def test_insufficient_balance(token, accounts):
    balance = token.balanceOf(accounts[1])
    
    with brownie.reverts("dev: Insufficient balance"):
        token.adminTransfer(accounts[1], accounts[2], balance + 100)