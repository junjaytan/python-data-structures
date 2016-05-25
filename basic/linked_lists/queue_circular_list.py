
class CircularQueue(object):
    """ Queue implementation using circularly linked list """

    def __init__(self):
        """ Create an empty queue """
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def peek(self):
        """ Return (but don't remove) element at front of queue """
        if self.is_empty():
            raise Exception("Queue is empty!")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """ Remove and return first element of the queue """
        if self.is_empty():
            raise Exception("Queue is empty!")
        oldhead = self._tail._next
        if self._size == 1:                     # queue becomes empty if removing the only element
            self._tail = None
        else:
            self._tail._next = oldhead._next    #bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """ Add an element to the back of queue """
        newest = self._Node(e, None)    # node will be new tail node
        if self.is_empty():
            newest._next = newest       # initialize circularly
        else:
            newest._next = self._tail._next     # new node points to head
            self._tail._next = newest           # old tail points to new node
        self._tail = newest                     # new node becomes tail
        self._size += 1

    def rotate(self):
        """ Rotate front element to back of queue """
        if self._size > 0:
            self._tail = self._tail._next



    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next       # next is a pointer to the next element

if __name__ == "__main__":
    myqueue = CircularQueue()