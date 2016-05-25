from priority_queue import PriorityQueueBase
from positional_list import PositionalList

class UnsortedPriorityQueue(PriorityQueueBase):
    """ a min-oriented priority queue implemented with an unsorted list """

    def __init__(self):
        """ Create a new empty Priority Queue """
        self._data = PositionalList()

    def _find_min(self):            # nonpublic utility
        """ Return Position of item with min key """
        if self.is_empty():         # method inherited from base class
            raise Exception('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)

    def __len__(self):
        """ Return the number of items in the priority queue. """
        return len(self._data)

    def add(self, key, value):
        """ add a key-value pair. """
        self._data.add_last(self._Item(key, value))

    def min(self):
        """ Return but do not remove (k,v) tuple with min key. """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """ Remove and return (k,v) tuple with min key. """
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
