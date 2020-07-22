class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, newValue):
        self.value = newValue

    def setNext(self, newNext):
        self.next = newNext
