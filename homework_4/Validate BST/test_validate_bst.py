from validate_bst import BSTNode, validate_bst

assert validate_bst(None) is True

root = BSTNode(5)
assert validate_bst(root) is True

root = BSTNode(4)
root.left = BSTNode(2)
root.right = BSTNode(6)
root.left.left = BSTNode(1)
root.left.right = BSTNode(3)
root.right.left = BSTNode(5)
root.right.right = BSTNode(7)
assert validate_bst(root) is True

root = BSTNode(5)
root.left = BSTNode(3)
root.right = BSTNode(4)  
assert validate_bst(root) is False

root = BSTNode(10)
root.left = BSTNode(5)
root.left.right = BSTNode(15)  
root.right = BSTNode(20)
assert validate_bst(root) is False

root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.right.left = BSTNode(8)  
assert validate_bst(root) is False

root = BSTNode(5)
root.left = BSTNode(4)
root.left.left = BSTNode(3)
root.left.left.left = BSTNode(2)
assert validate_bst(root) is True

root = BSTNode(1)
root.right = BSTNode(2)
root.right.right = BSTNode(3)
root.right.right.right = BSTNode(4)
assert validate_bst(root) is True

root = BSTNode(5)
root.left = BSTNode(5)  
assert validate_bst(root) is False
    
