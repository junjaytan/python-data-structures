""" Basic implementation of a singly linked list """

class SinglyLinkedList(object):
    def __init__(self):
        """ initialize empty list """
        self._head = None
        self._size = 0

    def list_search(self, k):
        """ finds first element with key k in list """
        x = self._head
        while (x is not None) and (x._element != k):
            x._next
        return x

    def list_insert(self, element):
        """ insert element onto the front of the linked list
        """

    def list_delete(self, element):
        """ given a pointer to x, splice x out of the list by updating pointers
        to delete an element with a given key, we must first call LIST_SEARCH
        to retrieve a pointer to the element
        can be simplified by using sentinels
        """


    class _Node(object):
        __slots__ = '_element', '_next' # streamline mem usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

if __name__ == "__main__":
    mylist = SinglyLinkedList()