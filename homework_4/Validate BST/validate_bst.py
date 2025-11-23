class BSTNode:
    __slots__ = ('key', 'left', 'right')
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def validate(node, min_val, max_val):
    if not node:
        return True
    
    if node.key <= min_val or node.key >= max_val:
        return False
    
    return (validate(node.left, min_val, node.key) and 
            validate(node.right, node.key, max_val))

def validate_bst(root):
    return validate(root, float('-inf'), float('inf'))