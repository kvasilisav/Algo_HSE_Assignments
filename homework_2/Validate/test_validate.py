from validate import validate

pushed = [1, 2, 3, 4, 5]
popped = [1, 3, 5, 4, 2]
assert validate(pushed, popped) is True

pushed = [1, 2, 3]
popped = [3, 1, 2]
assert validate(pushed, popped) is False

assert validate([], []) is True

assert validate([1], [1]) is True

pushed = [1, 2, 3, 4, 5]
popped = [5, 4, 3, 2, 1]
assert validate(pushed, popped) is True

pushed = [1, 2, 3, 4]
popped = [2, 4, 1, 3]
assert validate(pushed, popped) is False

n = 1000000
pushed = list(range(1, n + 1))
popped = list(range(n, 0, -1)) 
assert validate(pushed, popped) is True

pushed = [1, 2, 3, 4, 5, 6]
popped = [3, 2, 6, 5, 4, 1]
assert validate(pushed, popped) is True