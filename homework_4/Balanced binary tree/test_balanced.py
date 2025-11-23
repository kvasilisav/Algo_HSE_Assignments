from balanced import TreeNode, is_balanced

def create_tree(left_height, right_height):
    if left_height == 0 and right_height == 0:
        return TreeNode(0)
    
    root = TreeNode(0)
    if left_height > 0:
        root.left = create_tree(left_height - 1, left_height - 1)
    if right_height > 0:
        root.right = create_tree(right_height - 1, right_height - 1)
    return root

assert is_balanced(None) is True

assert is_balanced(TreeNode(1)) is True

balanced_deep = create_tree(5, 5)
assert is_balanced(balanced_deep) is True

almost_balanced = create_tree(4, 3)
assert is_balanced(almost_balanced) is True

unbalanced = create_tree(5, 3)
assert is_balanced(unbalanced) is False

left_empty = create_tree(0, 3)  
assert is_balanced(left_empty) is False

root = TreeNode(100)
root.left = create_tree(3, 3) 
root.right = TreeNode(200)
root.right.left = create_tree(2, 2)
root.right.right = create_tree(0, 3)  
assert is_balanced(root) is False
