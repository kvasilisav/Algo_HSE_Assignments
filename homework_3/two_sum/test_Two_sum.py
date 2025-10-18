from Two_sum import twosum

def test_twosum():
    assert twosum([1, 3, 4, 10], 7) == '1, 2'          
    assert twosum([5, 5, 1, 4], 10) == '0, 1'          
    assert twosum([0, 0], 0) == '0, 1'                  
    assert twosum([-5, 3, 10], 5) == '0, 2'            
    assert twosum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 17) == '7, 8'  
    assert twosum([-3, -2, -5], -7) == '1, 2'           
