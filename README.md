# Persistent Binary Search Tree (Fat Node Approach)

This project implements a **Persistent Binary Search Tree (BST)** using the **Fat Node** technique in Python. Persistence allows the tree to maintain access to its historical versions even after updates (insertions or deletions). This implementation is ideal for applications where versioned data access is important, such as time-travel debugging, undo functionality, or version control systems.

---

## ✨ Features

-  Fully persistent binary search tree using fat nodes
-  Versioned insert and delete operations
-  Search in any version of the tree
-  Pre-order, In-order, and Post-order traversal support
-  Demonstrative example included

---

## 📁 File Structure

- `FatNode`: Represents a node in the tree that stores historical values and children.
- `PersistentBST`: Handles version management, insertion, deletion, and traversal.
- Example usage at the bottom of the file demonstrates inserting, deleting, and printing at different versions.

---

## 🧠 How It Works

Each `FatNode` stores:
- A list of `(version, value)` pairs
- A list of `(version, left_node)` and `(version, right_node)` pairs

Instead of overwriting values or pointers, updates create a new version in the lists, allowing access to previous states.

Every time an insertion or deletion is made:
- A new version is created.
- The modified node is copied.
- The `root_versions` list is updated to point to the new root for that version.

---

## 🔧 Usage Example

```python
mylist = PersistentBST()

# Insert values
mylist.insert(5)
mylist.insert(3)
mylist.insert(7)
mylist.insert(2)
mylist.insert(4)
mylist.insert(6)
mylist.insert(8)

# Print latest version
mylist.print_list()

# Delete a value
mylist.delete(3)

# Print after deletion
mylist.print_list()

# Access historical versions
mylist.print_list(3)  # Before 3 was deleted
mylist.print_list(2)  # Tree after first two insertions
mylist.print_list(7)  # Full tree before any deletion

# Delete root
mylist.delete(5)
mylist.print_list()
