import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # because adding and removing is o(1)
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        if self.size > 0:                 
            self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size

    def print(self):
        self.storage.print()

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.print()

