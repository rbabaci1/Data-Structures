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
        self.set_head_tail(None, None)

    def set_head_tail(self, head_val, tail_val):
        self.head = head_val
        self.tail = tail_val

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.set_next(new_node)
            self.tail = new_node
        else:
            self.set_head_tail(new_node, new_node)

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            self.set_head_tail(new_node, new_node)

    def contains(self, value):
        if self.head:
            current_node = self.head
            while current_node:
                if current_node.get_value() == value:
                    return True
                current_node = current_node.get_next()
        return False

    def remove_head(self):
        if self.head and self.head.get_next():
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value
        elif self.head and not self.head.get_next():
            head_value = self.head.get_value()
            self.set_head_tail(None, None)
            return head_value

    def get_max(self):
        if self.head:
            current_node = self.head
            max_val = current_node.get_value()
            while current_node:
                if current_node.get_value() > max_val:
                    max_val = current_node.get_value()
                current_node = current_node.get_next()
            return max_val
