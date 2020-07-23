class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

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

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def contains(self, value):
        if not self.head:
            return False
        else:
            current_node = self.head
            while current_node:
                if current_node.get_value() == value:
                    return True
                current_node = current_node.get_next()
            return False

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

    def get_max(self):
        if not self.head:
            return None
        else:
            current_node = self.head
            max_val = current_node.get_value()
            while current_node:
                if current_node.get_value() > max_val:
                    max_val = current_node.get_value()
                current_node = current_node.get_next()
            return max_val
