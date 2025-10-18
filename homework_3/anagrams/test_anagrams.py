from anagrams import anagrams

def test_anagrams():
    assert sorted(map(sorted, anagrams(["eat","tea","tan","ate","nat","bat"]))) == [["ate","eat","tea"],["bat"],["nat","tan"]]
    assert anagrams([]) == []
    assert sorted(map(sorted, anagrams(["abc","bca","cab","abc"]))) == [["abc","abc","bca","cab"]]
    assert sorted(map(sorted, anagrams(["a","aa","aaa","b"]))) == [["a"],["aa"],["aaa"],["b"]]
    assert sorted(map(sorted, anagrams(["aab","aba","baa","abb","abc"]))) == [["aab","aba","baa"],["abb"],["abc"]]
    assert sorted(map(sorted, anagrams(["Listen","silent","123","321","Silent"]))) == [["123","321"],["Listen"],["Silent"],["silent"]]
    assert sorted(map(sorted, anagrams(["","a","a","cba","abc","bca"]))) == [[""],["a","a"],["abc","bca","cba"]]

test_anagrams()