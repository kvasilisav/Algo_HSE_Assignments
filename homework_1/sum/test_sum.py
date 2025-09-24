from sum import max_even_sum

def test_sum():
    assert max_even_sum([2, 4, 6, 8]) == 20
    assert max_even_sum([1, 3, 5, 7]) == 16  
    assert max_even_sum([3, 5, 7, 1, 9]) == 24 
    assert max_even_sum([3]) == 0  
    assert max_even_sum([2]) == 2
    assert max_even_sum([]) == 0 
    assert max_even_sum([1, 2, 3, 4, 5]) == 14  
    assert max_even_sum([0, 0, 0, 0]) == 0
    assert max_even_sum([0, 0, 0, 0, 2]) == 2
    assert max_even_sum([0, 0, 0, 0, 3]) == 0