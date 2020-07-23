from singly_linked_list import LinkedList
from stack import Stack
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Implemented using an array


class ArrayQueue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size:
            self.size -= 1
            return self.storage.pop(0)

# Implemented using a linked list


class QueueQueue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size:
            self.size -= 1
            return self.storage.remove_head()


# 3- The principal benefit of a linked list over an array, is that the list elements can be easily inserted or removed without reallocation or reorganization of the entire structure because the data items need not be stored contiguously in memory or on disk.
# When adding/removing elements from a linked list, the time complexity is O(1) vs O(n) in an array.

# Implemented using two stacks


class Queue:
    def __init__(self):
        self.size = 0
        self.inbox = Stack()
        self.outbox = Stack()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.inbox.push(value)

    def dequeue(self):
        if self.size:
            if self.outbox.isEmpty():
                while not self.inbox.isEmpty():
                    self.outbox.push(self.inbox.pop())
            self.size -= 1
            return self.outbox.pop()
