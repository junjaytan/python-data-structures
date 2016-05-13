
class LinkedListStack(object):
    """ LIFO Stack implementation using a singly linked list for storage """

    def __init__(self):
        """ Create an empty stack """
        self._head = None       # ref to head node
        self._size = 0          # num of stack elements

    def __len__(self):
        """ Return number of elements in the stack. """
        return self._size

    def is_empty(self):
        """" Return True if stack is empty """
        return self._size == 0

    def push(self, e):
        """ Add element e to the top of the stack. """
        self._head = self._Node(e, self._head)
        self._size += 1

    def peek(self):
        """ Return (but do not remove) element at top of the stack.
        Raise exception if stack is empty """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element      # top of stack is at head of list

    def pop(self):
        """ Remove and return the element from top of stack (i.e., LIFO) """
        if self.is_empty():
            raise Exception("Stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    class _Node(object):
        """ Lightweight, nonpublic class for storing a singly linked node. """
        __slots__ = '_element', '_next' # streamline mem usage

        def __init__(self, element, next):
            self._element = element     # ref to user's element
            self._next = next           # ref to next node



if __name__ == "__main__":
    mystack = LinkedListStack()
    mystack.push("a")
    mystack.push("b")
    mystack.push("c")
    print "top element is %s" % mystack.peek()
    print "popping top element: %s" % mystack.pop()
    print "top element is now %s" % mystack.peek()

    # the below just lists an object reference.
    #print mystack._head._next