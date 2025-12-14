from rabin_karp import rabin_karp

assert rabin_karp("", "abc") == []
assert rabin_karp("abc", "") == []
assert rabin_karp("", "") == []

assert rabin_karp("abc", "abcd") == []

assert rabin_karp("abc", "abc") == [0]

assert rabin_karp("ababab", "aba") == [0, 2]
assert rabin_karp("aaaaa", "aa") == [0, 1, 2, 3]

assert rabin_karp("abcdef", "xyz") == []

assert rabin_karp("Hello World", "world") == []
assert rabin_karp("Hello World", "World") == [6]

assert rabin_karp("a!b@c#", "!b@") == [1]

large_text = "a" * 10000
assert rabin_karp(large_text, "a" * 100) == list(range(9901))
