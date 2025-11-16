from AVL import AVL

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)

assert avl.search(30) is True
assert avl.search(100) is False
avl.delete(30)
assert avl.search(30) is False
avl.delete(10)
assert avl.search(10) is False
assert avl.search(25) is True
assert avl.search(50) is True