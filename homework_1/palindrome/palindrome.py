def is_palindrome(n: int) -> bool:
    if n < 0:
        return False

    original = n
    reversed_num = 0

    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10

    return original == reversed_num
