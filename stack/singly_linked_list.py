class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_value(self, newValue):
        self.value = newValue

    def set_next(self, newNext):
        self.next_node = newNext


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def remove_head(self):
        if not self.head:
            return None
        elif not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value
