from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# Implemented using a linked list as the storage


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.remove_head()

# Implemented using a list as the storage


class ArrayStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.pop()


# 3- The difference between using an array vs a linked list when implement the stack data structure is, when adding elements to the data structure, when using an array we append all new elements to the end of the array vs in a linked list items are added as heads.
# Also, when removing items from an array, we just pop the last item of the array since is the last element in vs in a linked list, we remove the head which was the last element in.
