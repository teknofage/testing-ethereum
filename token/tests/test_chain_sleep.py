def test_time_travel(accounts, chain):
    tx = accounts[0].transfer(accounts[1], "1 ether")
    
    # sleep for 1000 seconds
    chain.sleep(1000)
    
    next_tx = accounts[0].transfer(accounts[1], "1 ether")
    
    assert next_tx.timestamp >= tx.timestamp + 1000