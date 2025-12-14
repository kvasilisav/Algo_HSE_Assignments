from lcs import lcs

assert lcs("", "") == ""
assert lcs("", "abc") == ""
assert lcs("abc", "") == ""
assert lcs("a", "a") == "a"
assert lcs("a", "b") == ""

assert lcs("hello", "hello") == "hello"

assert lcs("ABCDGH", "AEDFHR") == "ADH"
assert lcs("AGGTAB", "GXTXAYB") == "GTAB"

assert lcs("123", "456") == ""

assert lcs("Hello", "hello") == "ello"
assert lcs("AbCdEf", "aBcDeF") == "" 
assert lcs("a!b@c#", "!@#") == "!@#"
assert lcs("кот", "скот") == "кот"

long_s1 = "A" * 1000 + "B" * 1000
long_s2 = "B" * 1000 + "A" * 1000
assert lcs(long_s1, long_s2) == "A" * 1000 or lcs(long_s1, long_s2) == "B" * 1000

result = lcs("ABCBDAB", "BDCABA")
assert result == "BDAB" 
