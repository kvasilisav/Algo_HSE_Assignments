from prime import prime_amount as prime
from brutforce import brutforce_prime_amount as brutforce
import random

def test_prime():
    for _ in range(20):
        n = random.randint(0, 1000)
        assert prime(n) == brutforce(n)