# see: http://learnpythonthehardway.org/book/ex44.html

# example of inheritance
class Employee(object):
    def __init__(self, rank=0):
        self.rank = rank
        self.handling_call = False
        self._calls = []

    def get_rank(self):
        return self.rank

    def receive_call(self, call):
        """ takes a call object. update call status. For simulation purposes, maybe set call to be handled after some random time between x and y """
        self._calls.append(call)
        self.handling_call = True

    def is_busy(self):
        """ returns true if handling a call. returns false if able to handle a call """
        return self.handling_call

class JuniorEmployee(Employee):
    def __init__(self):
        self.rank = 0

class MiddleManager(Employee):
    def __init__(self):
        super(MiddleManager, self).__init__()       # need to initialize the parent class to access its properties
        self.rank = 1

class Executive(Employee):
    def __init__(self):
        # note that this child class doesn't have access to any of the parent's properties because
        self.rank = 2


mymiddlemanager = MiddleManager()
print mymiddlemanager.get_rank()
print mymiddlemanager.is_busy()
mymiddlemanager.receive_call("hello")
print mymiddlemanager.is_busy()