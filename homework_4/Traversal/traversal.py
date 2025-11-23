class BSTNode:
    __slots__ = ('key', 'left', 'right')
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)
    
    def pre_order(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result
    
    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)
    
    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result
    
    def _post_order_recursive(self, node, result):
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.key)
    
    def in_order(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result
    
    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.key)
            self._in_order_recursive(node.right, result)
    
    def reverse_pre_order(self):
        result = []
        self._reverse_pre_order_recursive(self.root, result)
        return result
    
    def _reverse_pre_order_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._reverse_pre_order_recursive(node.right, result)
            self._reverse_pre_order_recursive(node.left, result)
    
    def reverse_post_order(self):
        result = []
        self._reverse_post_order_recursive(self.root, result)
        return result
    
    def _reverse_post_order_recursive(self, node, result):
        if node:
            self._reverse_post_order_recursive(node.right, result)
            self._reverse_post_order_recursive(node.left, result)
            result.append(node.key)
    
    def reverse_in_order(self):
        result = []
        self._reverse_in_order_recursive(self.root, result)
        return result
    
    def _reverse_in_order_recursive(self, node, result):
        if node:
            self._reverse_in_order_recursive(node.right, result)
            result.append(node.key)
            self._reverse_in_order_recursive(node.left, result)