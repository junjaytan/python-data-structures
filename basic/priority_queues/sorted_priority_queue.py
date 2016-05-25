from priority_queue import PriorityQueueBase
from positional_list import PositionalList

class SortedPriorityQueue(PriorityQueueBase):   # base class defines _Item
    """ A min-oriented priority queue implemented with a sorted list. """

    def __init__(self):
        """ Create a new empty Priority Queue. """
        self._data = PositionalList()

    def __len__(self):
        """ Return the num of items in the priority queue. """
        return len(self._data)

    def add(self, key, value):
        """ Add a key-value pair. """
        newest = self._Item(key, value)         # make new item instance
        walk = self._data.last()                # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)        # new key is smallest
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        """ Return but do not remove (k,v) tuple with min key """
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """ Remove and return (k,v) tuple with min key. """
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
