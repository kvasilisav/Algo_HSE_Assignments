from palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(12321) == True
    assert is_palindrome(10) == False
    assert is_palindrome(2) == True
    assert is_palindrome(123) == False
    assert is_palindrome(123321) == True
    assert is_palindrome(12345) == False
    assert is_palindrome(0) == True
    assert is_palindrome(111111111) == True
    assert is_palindrome(1001) == True
    assert is_palindrome(1010) == False
