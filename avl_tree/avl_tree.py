"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = AVLTree()
        self.right = AVLTree()


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
        self.update_height()
        self.update_balance()

        if self.node:
            print(
                "-" * level * 2,
                pref,
                self.node.key,
                f"[{self.height}:{self.balance}]",
                "L" if self.height == 0 else " ",
            )
            if self.node.left.node:
                self.node.left.display(level + 1, "<")
            if self.node.right.node:
                self.node.right.display(level + 1, ">")

    """
    Computes the maximum number of levels there are
    in the tree
    """

    def update_height(self):
        root = self.node
        if root.left.node and root.right.node:
            self.height = max(root.left.update_height(), root.right.update_height()) + 1
            return self.height
        if root.left.node:
            self.height = root.left.update_height() + 1
            return self.height
        if root.right.node:
            self.height = root.right.update_height() + 1
            return self.height
        else:
            self.height = 0
            return self.height

    """
    Updates the balance factor on the AVLTree class
    """

    def update_balance(self):
        if self.node.left.node:
            self.node.left.update_balance()
        if self.node.right.node:
            self.node.right.update_balance()

        left_height = -1
        right_height = -1
        if self.node.left.node:
            left_height = self.node.left.height
        if self.node.right.node:
            right_height = self.node.right.height
        self.balance = left_height - right_height

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """

    def left_rotate(self):
        root = self.node
        new_root = root.right.node
        new_root_left = new_root.left.node

        self.node = new_root
        root.right.node = new_root_left
        new_root.left.node = root

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """

    def right_rotate(self):
        root = self.node
        new_root = root.left.node
        new_root_right = new_root.right.node

        self.node = new_root
        root.left.node = new_root_right
        new_root.right.node = root

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """

    def rebalance(self):
        left_node = self.node.left.node
        right_node = self.node.right.node
        self.update_height()
        self.update_balance()

        if left_node:
            self.node.left.rebalance()
        if right_node:
            self.node.right.rebalance()

        if abs(self.balance) > 1:
            if self.balance > 0:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                self.right_rotate()
            else:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                self.left_rotate()

    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """

    def insert(self, key):
        if self.node:
            if key < self.node.key:
                self.node.left.insert(key)
            else:
                self.node.right.insert(key)
        else:
            self.node = Node(key)
        self.rebalance()
