"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def set_head_tail(self, head_val, tail_val):
        self.head = head_val
        self.tail = tail_val

    @staticmethod
    def delete_node(node):
        node.prev = None
        node.next = None

    def swap_head_tail(self):
        head_value = self.head.value
        self.head.value = self.tail.value
        self.tail.value = head_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value, rst=0):
        new_node = ListNode(value, None, self.head)
        if not self.length:
            self.set_head_tail(new_node, new_node)
        else:
            self.head.prev = new_node
            self.head = new_node
        self.length += 1 - rst

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        head_value = None
        if not self.head:
            return None
        elif not self.head.next:
            head_value = self.head.value
            self.set_head_tail(None, None)
        else:
            head_value = self.head.value
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
        self.length -= 1
        return head_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value, rst=0):
        new_node = ListNode(value, None, self.tail)
        if not self.length:
            self.set_head_tail(new_node, new_node)
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 - rst

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        tail_value = None
        if not self.tail:
            return None
        elif not self.head.next:
            tail_value = self.tail.value
            self.set_head_tail(None, None)
        else:
            tail_value = self.tail.value
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
        self.length -= 1
        return tail_value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head:
            if self.length == 2:
                self.swap_head_tail()
            else:
                current = self.head
                while current:
                    if current == node:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        self.add_to_head(current.value, 1)
                        self.delete_node(current)
                        break
                    current = current.next

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.tail:
            if self.length == 2:
                self.swap_head_tail()
            else:
                current = self.head
                while current:
                    if current == node:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        self.add_to_tail(current.value, 1)
                        self.delete_node(current)
                        break
                    current = current.next

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass
