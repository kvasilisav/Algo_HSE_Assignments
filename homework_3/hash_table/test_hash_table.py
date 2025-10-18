from hash_table import HashTable

def test_hash_table():
    ht = HashTable()

    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("c", 3)
    assert ht.find("a") == 1
    assert ht.find("b") == 2
    assert ht.find("c") == 3
    assert ht.find("d") is None

    ht.insert("a", 10)
    assert ht.find("a") == 10
    assert ht.size == 3

    assert ht.delete("b") is True
    assert ht.find("b") is None
    assert ht.size == 2
    assert ht.delete("x") is False  

    ht.insert("d", 4)
    assert ht.find("d") == 4
    assert ht.size == 3

    keys = [f"key{i}" for i in range(10)]
    for i, k in enumerate(keys):
        ht.insert(k, i)
    assert ht.size == 13 
    for i, k in enumerate(keys):
        assert ht.find(k) == i

    s = str(ht)
    assert s.startswith("{")
    assert s.endswith("}")
    assert "a: 10" in s
    assert "key9: 9" in s

    ht.delete("key0")
    s2 = str(ht)
    assert "key0:" not in s2

test_hash_table()