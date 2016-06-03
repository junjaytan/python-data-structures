import random

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

    def create_id(self):
        self.id = random()


class MiddleManager(Employee):
    def __init__(self):
        super(MiddleManager, self).__init__()       # need to initialize the parent class to access its properties
        self.rank = 1

class Executive(Employee):
    def __init__(self):
        # note that this child class doesn't have access to any of the parent's properties because
        self.rank = 2
        self._report = None

    def write_report(self):
        self._report = Report()

    def write_report_item(self, item):
        self._report.add_item(item)

    def inherit_report(self, report):
        """ executive inherits a report object from someone else"""
        self._report = report

    def get_report_items(self):
        return self._report.get_items()

class Report(object):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items