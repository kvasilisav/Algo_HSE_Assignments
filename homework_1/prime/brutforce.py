def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def brutforce_prime_amount(n: int) -> int:
    counter = 0
    for i in range(1, n):
        counter += int(is_prime(i))                
    return counter


