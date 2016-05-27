class SinglyLinkedListQueue(object):
    """ FIFO queue implementation using a singly linked list for storage
    natural orientation is to align the front of the queue with the head of the list,
    and the back of the queue with the tail of the list
    because we must be able to enqueue elements at the back
    and dequeue them from the front
    """

    def __init__(self):
        """ Create an empty queue """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ override len method to return the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ return True if queue is empty """
        return self._size == 0

    def first(self):
        """ Return (but do not remove) the element at the front of the queue """
        if self.is_empty():
            raise Exception("Queue is empty!")
        return self._head._element              # front aligned with head of list

    def dequeue(self):
        """ Remove and return the first element of the queue (FIFO)
        i.e., remove head node """
        if self.is_empty():
            raise Exception("Queue is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            # special case as queue is empty removed head had been the tail
            self._tail = None
        return answer

    def enqueue(self, e):
        """ Add an element to the back of queue (i.e., tail of the list). """
        newest = self._Node(e, None)        # node will be new tail node
        if self.is_empty():                 # special case: previously empty
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    class _Node(object):
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

if __name__ == "__main__":
    myqueue = SinglyLinkedListQueue()
    myqueue.enqueue("a")

    myqueue.enqueue("b")
    print myqueue.first()

    myqueue.dequeue()
    myqueue.dequeue()
