
# 3.1
class ThreeStackOneArray(object):
    """

    """



# 3.3
class SetOfStacks(object):
    def __init__(self, max_stack_size):
        self._max_stack_size = max_stack_size               # max size per individual stack
        self._substacks = []                                # list of stack objects
        self._current_stack_index = 0                       # pointer to current stack

    def push(self, element):
        """ push element onto stack """

        # if first element, create an initial stack to hold elements
        if len(self._substacks) == 0:
            self._substacks.append(self.Stack(self._max_stack_size))        # add a new Stack object to the list
            self._substacks[0].push(element)                                # push a new element to that Stack
        else:
            if self._substacks[self._current_stack_index].size() == self._max_stack_size:     # if current stack is full
                self._substacks.append(self.Stack(self._max_stack_size))                    # add a new stack
                self._current_stack_index += 1
            self._substacks[self._current_stack_index].push(element)


    def pop(self):
        """ delete element from stack. If current stack is empty, remove that stack and proceed onto previous stack"""
        if len(self._substacks) == 0:
            raise Exception('Stack is empty.')
        else:
            if self._substacks[self._current_stack_index].size() == 1:        # if last element in current stack,
                deleted_element = self._substacks[self._current_stack_index].pop()
                self._substacks.pop(self._current_stack_index)              # remove the empty stack
                self._current_stack_index -= 1
            else:
                deleted_element = self._substacks[self._current_stack_index].pop()
            return deleted_element

    def peek(self):
        return self._substacks[self._current_stack_index].peek()

    def pop_at(self, stack_index):
        """ pop element in a specific stack """
        if stack_index not in range(0,self._current_stack_index):
            raise Exception('Invalid stack index')
        else:
            if stack_index == self._current_stack_index:        # if user is popping from current stack, proceed as usual
                self.pop()
            else:
                raise NotImplementedError('need to implement popAt method')
                """
                # otherwise pop from designated stack and rearrange elements among stacks
                self._substacks[stack_index].pop()
                                                                # now use stack operations to rearrange elements among stacks by creating a new temp stack
                for index in range(stack_index + 1, self._current_stack_index):
                    temp_stack = self.Stack()
                    # transfer all elements except first element from next stack to temp stack
                    for i in range(0,self._substacks[index].size()):
                        self._substacks[]
                """
                # alternatively use python list methods to more directly access the bottom-most stack element of the next stack



    class Stack(object):
        def __init__(self, max_size, next_stack=None):
            self.elements = []  # initialize empty list to hold elements
            self._max_size = max_size                       # max size of stack
            self._size = 0                                  # current size of stack

        def push(self, element):
            if self._size == self._max_size:
                raise Exception('Stack is full')
            else:
                self.elements.append(element)
                self._size += 1

        def pop(self):
            """ remove top element and return it """
            if self._size == 0:
                raise Exception('Stack is empty')
            else:
                self._size -= 1
                return self.elements.pop(0)

        def peek(self):
            return self.elements[len(self.elements)-1]

        def size(self):
            return self._size

        def next_stack(self):
            return self._next_stack

mystack = SetOfStacks(2)
mystack.push("hi")
mystack.push("yo")
print mystack._current_stack_index
mystack.push("hello")
print mystack._current_stack_index
print mystack.pop()
print mystack._current_stack_index
#mystack.push("there")
#print mystack.peek()