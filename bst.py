class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            print("Value already in tree!")

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.find(value)
        else:
            return True

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Case 1: No child
            if self.left is None and self.right is None:
                return None
            # Case 2: One child
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # Case 3: Two children
            min_larger_node = self.right.find_min()
            self.value = min_larger_node.value
            self.right = self.right.delete(min_larger_node.value)
        return self

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.value, end=" -> ")
        if self.right:
            self.right.in_order()

    def pre_order(self):
        print(self.value, end=" -> ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.value, end=" -> ")


# Optional wrapper class to mimic PersistentBST structure
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def find(self, value):
        if self.root is None:
            return False
        return self.root.find(value)

    def delete(self, value):
        if self.root is not None:
            self.root = self.root.delete(value)

    def print_in_order(self):
        if self.root:
            self.root.in_order()
        print("None")

    def print_pre_order(self):
        if self.root:
            self.root.pre_order()
        print("None")

    def print_post_order(self):
        if self.root:
            self.root.post_order()
        print("None")
