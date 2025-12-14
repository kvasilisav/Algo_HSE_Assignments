from kmp import kmp_search

assert kmp_search("", "abc") == []
assert kmp_search("abc", "") == []
assert kmp_search("", "") == []

assert kmp_search("abc", "abcd") == []

assert kmp_search("abc", "abc") == [0]

assert kmp_search("ababab", "aba") == [0, 2]
assert kmp_search("aaaaa", "aa") == [0, 1, 2, 3]

assert kmp_search("abcdef", "xyz") == []

assert kmp_search("Hello World", "world") == []
assert kmp_search("Hello World", "World") == [6]

assert kmp_search("a!b@c#", "!b@") == [1]

large_text = "a" * 10000
assert kmp_search(large_text, "a" * 100) == list(range(9901))