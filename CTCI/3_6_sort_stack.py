#3.6: sort a Stack using only stack operations push, pop, peek, and is_empty
class Stack(object):
    def __init__(self):
        """ intializes a new stack that is empty (as a primitive python list) """
        self.items = []

    def push(self, item):
        """ add new item to top of stack """
        self.items.append(item)

    def pop(self):
        """ removes the last item from the stack, and returns it """
        if (self.stack_empty() == True):
            raise Exception("Error: Trying to pop an empty stack")
        else:
            return self.items.pop()

    def pop2(self):
        """ alternative implementation of pop that doesn't use the inbuilt pop method """
        last_index = len(self.items)

        last_element = self.items[last_index-1]
        del self.items[last_index-1]
        return last_element

    def peek(self):
        """ return the last element in stack """
        if (self.stack_empty() == True):
            return None
        else:
            return self.items[len(self.items)-1]

    def stack_empty(self):
        """ returns whether stack is empty """
        if len(self.items) == 0:
            return True
        else:
            return False

    def stack_size(self):
        """ return size of stack """
        return len(self.items)

def sort_stack_nonrecursive(s):
    temp_stack = Stack()
    while not s.stack_empty():
        current_element = s.pop()
        while not temp_stack.stack_empty() and temp_stack.peek() > current_element:
            s.push(temp_stack.pop())
        temp_stack.push(current_element)

    return temp_stack


def sort_stack_recursive(s):
    temp_stack = Stack()            # initialize a new temp stack

    while not s.stack_empty():
        top_element = s.pop()
        sorted_insert_recursive(s, temp_stack, top_element)

    """
        sorted_insert_recursive(s, temp_stack, last_element)
    """
    return s

def sorted_insert_recursive(orig_stack, temp_stack, element):
    # push element onto temp stack into the correct position, or recurse until that occurs and then push back elements
    if temp_stack.stack_empty() or element > temp_stack.peek():     # if temp stack is empty or placing element meets sorted condition, add to stack
        temp_stack.push(element)
    else:                                                           #otherwise
        orig_stack.push(temp_stack.pop())                           # push element from temp stack back onto orig stack
        sorted_insert_recursive(orig_stack, temp_stack, element)                                   # and recurse until you have a sorted stack with the new element



if __name__ == "__main__":
    mystack = Stack()
    mystack.push(1)
    mystack.push(10)
    mystack.push(3)
    mystack.push(4)
    print "orig stack: " + str(mystack.items)
    #print sort_stack(mystack).items

    """
    stack2 = Stack()
    stack2.push(3)
    stack2.push(5)
    print "secondary stack: " + str(stack2.items)


    element = mystack.pop()
    print "popping element: " + str(element)
    sorted_insert_recursive(mystack, stack2, element)
    print mystack.items
    print stack2.items
    """
    mysorted = sort_stack_nonrecursive(mystack)
    print "sorted stack: " + str(mysorted.items)