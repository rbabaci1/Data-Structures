"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """

    def display(self, level=0, pref=""):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print(
                "-" * level * 2,
                pref,
                self.node.key,
                f"[{self.height}:{self.balance}]",
                "L" if self.height == 0 else " ",
            )
            if self.node.left != None:
                self.node.left.display(level + 1, "<")
            if self.node.right != None:
                self.node.right.display(level + 1, ">")

    """
    Computes the maximum number of levels there are
    in the tree
    """

    def update_height(self):
        if self.node.left and self.node.right:
            self.height = (
                max(self.node.left.update_height(), self.node.right.update_height()) + 1
            )
            return self.height
        if self.node.left:
            self.height = self.node.left.update_height() + 1
            return self.height
        if self.node.right:
            self.height = self.node.right.update_height() + 1
            return self.height
        else:
            self.height = 0
            return self.height

    """
    Updates the balance factor on the AVLTree class
    """

    def update_balance(self):
        pass

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """

    def left_rotate(self):
        new_root = self.node.right
        self.node.right = new_root.left
        new_root.left = self.node

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """

    def right_rotate(self):
        new_root = self.node.left
        self.node.left = new_root.right
        new_root.right = self.node
        self.height = max(self.node.left.height, self.node.right.height) + 1
        new_root.height = max(new_root.node.left.height, new_root.node.right.height) + 1
        return new_root

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """

    def rebalance(self):
        pass

    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """

    def insert(self, key):
        if not self.node:
            self.node = Node(key)
        else:
            if key < self.node.key:
                if not self.node.left:
                    self.node.left = AVLTree(Node(key))
                else:
                    self.node.left.insert(key)
            else:
                if not self.node.right:
                    self.node.right = AVLTree(Node(key))
                else:
                    self.node.right.insert(key)
