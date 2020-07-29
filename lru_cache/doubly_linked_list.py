class Node:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
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
