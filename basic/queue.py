class Queue(object):
    """ Assumes front of the list is element 0 """
    def __init__(self):
        """ """
        self.items = []

    def enqueue(self, item):
        """"""
        self.items.append(item)

    def dequeue(self):
        """ removes first item from list and returns it """
        if self.is_empty() == True:
            raise Exception("Error: Cannot dequeue an empty queue")
        else:
            first_element = self.items[0]
            del self.items[0]
            return first_element

    def is_empty(self):
        """"""
        if len(self.items) == 0:
            return True
        else:
            return False

if __name__ == "__main__":

    my_queue = Queue()
    my_queue.enqueue("a")
    my_queue.enqueue("b")
    print my_queue.items
    my_queue.dequeue()
    print my_queue.items


