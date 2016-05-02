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

if __name__ == "__main__":
    mystack = Stack()
    #mystack.push("a")
    #mystack.push("b")

    print mystack.items

    poppedelement = mystack.pop()
    #print poppedelement
    #print mystack.items
