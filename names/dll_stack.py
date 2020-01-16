import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.dbly_list = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.size += 1
        self.dbly_list.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.dbly_list.remove_from_head()

    def len(self):
        return self.size
