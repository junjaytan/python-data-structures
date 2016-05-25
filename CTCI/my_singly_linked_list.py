# Implementation of Singly Linked List for exercises in Ch 2

class SinglyLinkedList(object):

    def __init__(self):
        """ initialize empty list """
        self._head = None
        self._size = 0      # initialize size

        self.insert(None)   # insert sentinel node
        self._size = 0      # reset size to 0 (i.e., ignore sentinel node)

    def insert(self, key, beforekey = None):
        """
        Inserts new element. By default, inserts element at head of list
        If beforekey is specified, inserts new element somewhere within the list
        before first appearance of designated key, which can take up to O(n) time
        """
        if beforekey == None:
            new_node = self._Node(key, self._head)
            self._head = new_node
        else:
            raise NotImplementedError()

        self._size += 1


    def delete(self, key = None):
        """
        Delete first appearance of item with given key. Worst case is O(n) because must search
        Return deleted element
        """
        if self._size == 0:                         # nothing to delete
            raise Exception('List is empty. Nothing to delete!')
        elif (key == None or key == self._head._key) and self._size > 0:
            """
            delete first element of list (i.e., the head) if no key is specified, or if key is found in head
            """
            element_to_delete = self._head
            self._head = element_to_delete._next
            print "deleted element with key: %s" % element_to_delete._key
            return element_to_delete
        else:
            element_to_delete = self.search(key)
            if element_to_delete == None:           # element not found
                print "Not found, so could not delete element with key: %s" % str(key)
                return None
            else:
                # recurse to find previous element and link it to the next element.
                next_element = element_to_delete._next
                prev_element = self._find_previous(element_to_delete)
                prev_element._next = next_element
                print "deleted element with key: %s" % element_to_delete._key
                return element_to_delete


    def _find_previous(self, next_element):
        current = self._head
        while current._next is not next_element:
            current = current._next
        return current

    def search(self, key):
        """
        Finds first appearance of key. Returns the node object or None if not found
        """
        n = 0       # index to count how many hops it takes to find the key

        # if empty, return None
        # while not at final sentinel node and node key != desired key, continue to next
        #       return key if found
        # otherwise return None
        if self._size == 0:
            print "empty list!"
            return None
        else:
            current = self._head      # start at head
            while (current._key is not None) and (current._key != key):
                current = current._next
                n += 1
            if current._key == key:
                n += 1
                print "node found!"
                print "at node %s from the head" % str(n)
                return current
            else:
                print "node NOT found!"
                return None

    class _Node(object):

        __slots__ = '_key', '_next'     # streamline mem usage

        def __init__(self, key, next):
            self._key = key
            self._next = next   # pointer to next node


if __name__ == "__main__":
    # TODO: add some unit tests
    mylist = SinglyLinkedList()
    mylist.insert("yo")
    mylist.insert("hello")
    mylist.insert("there")
    mylist.insert("whoop")
    #print mylist._size

    mylist.search("hello")
    mylist.delete("hello")
    mylist.delete("hello")