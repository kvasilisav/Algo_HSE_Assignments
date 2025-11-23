from traversal import BST

bst = BST()
assert bst.pre_order() == []
assert bst.post_order() == []
assert bst.in_order() == []
assert bst.reverse_pre_order() == []
assert bst.reverse_post_order() == []
assert bst.reverse_in_order() == []

bst = BST()
bst.insert(10)
assert bst.pre_order() == [10]
assert bst.post_order() == [10]
assert bst.in_order() == [10]
assert bst.reverse_pre_order() == [10]
assert bst.reverse_post_order() == [10]
assert bst.reverse_in_order() == [10]

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)

assert bst.pre_order() == [4, 2, 1, 3, 6, 5, 7]
assert bst.post_order() == [1, 3, 2, 5, 7, 6, 4]
assert bst.in_order() == [1, 2, 3, 4, 5, 6, 7]
assert bst.reverse_pre_order() == [4, 6, 7, 5, 2, 3, 1]
assert bst.reverse_post_order() == [7, 5, 6, 3, 1, 2, 4]
assert bst.reverse_in_order() == [7, 6, 5, 4, 3, 2, 1]

bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)

assert bst.pre_order() == [1, 2, 3, 4]
assert bst.post_order() == [4, 3, 2, 1]
assert bst.in_order() == [1, 2, 3, 4]
assert bst.reverse_pre_order() == [1, 2, 3, 4]
assert bst.reverse_post_order() == [4, 3, 2, 1]
assert bst.reverse_in_order() == [4, 3, 2, 1]

bst = BST()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)

assert bst.pre_order() == [4, 3, 2, 1]
assert bst.post_order() == [1, 2, 3, 4]
assert bst.in_order() == [1, 2, 3, 4]
assert bst.reverse_pre_order() == [4, 3, 2, 1]
assert bst.reverse_post_order() == [1, 2, 3, 4]
assert bst.reverse_in_order() == [4, 3, 2, 1]

bst = BST()
bst.insert(5)
bst.insert(5)
bst.insert(5)

assert bst.pre_order() == [5]
assert bst.post_order() == [5]
assert bst.in_order() == [5]
assert bst.reverse_pre_order() == [5]
assert bst.reverse_post_order() == [5]
assert bst.reverse_in_order() == [5]