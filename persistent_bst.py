class FatNode:
    def __init__(self, value, version):
        "Initializing a persistent node for a binary search tree."
        self.value_versions = [(version, value)]  # Stores (version, value)
        self.left_versions = [(version, None)]  # Stores (version, left_node)
        self.right_versions = [(version, None)]  # Stores (version, right_node)

    def get_value(self, version):
        "Retrieve the value at a given version."
        for t, v in reversed(self.value_versions):
            if t <= version:
                return v
        return None #Something might be wrong

    def get_left(self, version):
        "Retrieve the left node at a given version. "
        for t, n in reversed(self.left_versions):
            if t <= version:
                return n
        return None #Something might be wrong

    def get_right(self, version):
        "Retrieve the right node at a given version. "
        for t, n in reversed(self.right_versions):
            if t <= version:
                return n
        return None #Something might be wrong

    def set_value(self, version, value):
        """Update the value in the fat node at a new version."""
        self.value_versions.append((version, value))

    def set_left(self, version, left_node):
        """Update the left pointer at a new version."""
        self.left_versions.append((version, left_node))

    def set_right(self, version, right_node):
        """Update the right pointer at a new version."""
        self.right_versions.append((version, right_node))


class PersistentBST:
    def __init__(self):
        "Anytime something changes in the tree, we version the root. "
        self.version = 0 # Initial version
        self.root_versions = [(self.version, None)]


    def get_root(self, version):
        "Retrieve the BST root at a given version."
        for t, h in reversed(self.root_versions):
            if t <= version:
                return h
        return None


    def insert(self, value):
        "Increments the list's version, and calls the recursive insert function"
        "to decide if the new node will be on the left of the tree or right"
        self.version += 1
        current_root = self.get_root(self.version - 1)
        new_root = self._insert_rec(current_root, value, self.version)
        self.root_versions.append((self.version, new_root))


    def _insert_rec(self, current, value, version):
      "Function to insert a new node into the BST recursively."
      if current is None:
          return FatNode(value, version)

      #Copying the old node to maintain persistence
      new_node = FatNode(current.get_value(version - 1), version)
      if value < current.get_value(version - 1):
          # Insert in left subtree
          new_node.set_left(version, self._insert_rec(current.get_left(version - 1), value, version))
          new_node.set_right(version, current.get_right(version - 1))  # Copy right pointer
      else:
          # Insert in right subtree
          new_node.set_right(version, self._insert_rec(current.get_right(version - 1), value, version))
          new_node.set_left(version, current.get_left(version - 1))  # Copy left pointer

      return new_node


    def delete(self, value):
        """Delete from the persistent BST by calling the recursive delete function."""
        self.version += 1
        current_root = self.get_root(self.version - 1)
        new_root = self._delete_rec(current_root, value, self.version)
        self.root_versions.append((self.version, new_root))


    def _delete_rec(self, current, value, version):
      "Function to delete a node from the BST recursively."
      if current is None:
          return None
      new_node = FatNode(current.get_value(version - 1), version) #copy the node
      if value < current.get_value(version - 1):
          # Delete from left
          new_node.set_left(version, self._delete_rec(current.get_left(version - 1), value, version))
          new_node.set_right(version, current.get_right(version - 1))  # Copy right pointer
      elif value > current.get_value(version - 1):
          # Delete from right
          new_node.set_right(version, self._delete_rec(current.get_right(version - 1), value, version))
          new_node.set_left(version, current.get_left(version - 1))  # Copy left pointer
      else:
          # Found the node to delete
          left = current.get_left(version - 1)
          right = current.get_right(version - 1)
          if left is None:
              return right
          elif right is None:
              return left

          #find the successor, When deleting a node with two children, we need to find the next highest
          successor = self.find_min(current.get_right(version - 1), version)
          new_node.set_value(version, successor.get_value(version - 1)) #replacing the value
          new_node.set_right(version, self._delete_rec(current.get_right(version - 1), successor.get_value(version - 1), version))
          new_node.set_left(version, current.get_left(version - 1))

      return new_node


    def find_min(self, current, version):
      "Find the minimum value node in a subtree."
      while current.get_left(version) is not None:
          current = current.get_left(version)
      return current


    def search(self, value, version=None):
        "Serach a value in the persistent BST at the given version"
        if version is None:
            version = self.version
        current = self.get_root(version)

        while current:
            if current.get_value(version) == value:
                return True
            elif value < current.get_value(version):
                current = current.get_left(version)
            else:
                current = current.get_right(version)
        return False


    def print_list(self, version=None):
        "Print persistent BST in-order traversal"
        if version is None:
            version = self.version
        self._print_pre_order(self.get_root(version), version)
        print("None")


    def _print_in_order(self, node, version):
        "Recursive function to print the BST in-order"
        if node is None:
            return
        self._print_in_order(node.get_left(version), version)
        print(node.get_value(version), end=" -> ")
        self._print_in_order(node.get_right(version), version)

    def _print_pre_order(self, node, version):
        "Recursive function to print the BST pre-order"
        if node is None:
            return
        print(node.get_value(version), end=" -> ")
        self._print_pre_order(node.get_left(version), version)
        self._print_pre_order(node.get_right(version), version)

    def _print_post_order(self, node, version):
        "Recursive function to print the BST post-order"
        if node is None:
            return
        print(node.get_value(version), end=" -> ")
        self._print_post_order(node.get_left(version), version)
        self._print_post_order(node.get_right(version), version)


#example

mylist=PersistentBST()
mylist.insert(5)
mylist.insert(3)
mylist.insert(7)
mylist.insert(2)
mylist.insert(4)
mylist.insert(6)
mylist.insert(8)
mylist.print_list()

mylist.delete(3)
mylist.print_list()

mylist.print_list(3)
mylist.print_list(2)
mylist.print_list(7)

mylist.delete(5)
mylist.print_list()
