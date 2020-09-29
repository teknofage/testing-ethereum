def test_mine_blocks(accounts, chain):
    tx = accounts[0].transfer(accounts[1], "1 ether")
    
    # mine 100 blocks
    chain.mine(100)
    
    assert chain[-1].number == tx.block_number + 100