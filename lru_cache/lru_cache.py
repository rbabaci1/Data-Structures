class Node:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def swap_head_tail(self):
        value = self.head.value
        self.head.value = self.tail.value
        self.tail.value = value

    def add_as_head(self, key, value, opt=0):
        new_node = Node(key, value, None, self.head)
        if self.length:
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1 - opt

    def remove_tail(self):
        if self.head and self.head.next:
            self.tail = self.tail.prev
            self.tail.next = None
        elif self.head and not self.head.next:
            self.head = self.tail = None
        self.length -= 1

    def move_to_front(self, key):
        if self.head:
            if key == self.head.key:
                return
            if self.length == 2 and key == self.tail.key:
                self.swap_head_tail()
            elif self.length > 2 and key == self.tail.key:
                self.add_as_head(self.tail.key, self.tail.value, 1)
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                current = self.head
                while current:
                    if current.key == key:
                        self.add_as_head(current.key, current.value, 1)
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        break
                    current = current.next


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            value = self.storage[key]
            del self.storage[key]
            self.list.move_to_front(key)
            self.storage[key] = value
            return self.storage[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.storage:
            self.storage[key] = value
            self.list.move_to_front(key)
        else:
            if self.length == self.limit:
                self.list.remove_tail()
                del self.storage[next(iter(self.storage))]
                self.length -= 1
            self.list.add_as_head(key, value)
            self.storage[key] = value
            self.length += 1

