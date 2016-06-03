# 7.2
class CallCenter(object):
    def __init__(self):
        # initialize new empty call center
        self._freshers = []
        self._tl_pm = []
        self._employee_capacity = 10

    def add_employee(self, employee):
        if (len(self._freshers) + len(self._tl_pm)) < 10:
            if employee.rank < 1:
                self._freshers.append(employee)
            elif employee.rank > 1 and len(
                    self._tl_pm) == 0:  # if its a TL or PM we have to verify we can add this since we can only have one
                self._tl_pm.append(employee)
            else:
                raise Exception("Call center employee count isn't at capacity, but can't add another PM or TL")
        else:
            raise Exception("Call center is at capacity. Can't add more employees")

    def remove_employee(self, index=0):
        """ remove a specific employee or a random employee.
            if employee to be removed is TL or PM, adjust the count accordingly
        """

    def get_call_handler(self, call):
        """ receives a call and routes to the appropriate employee, or puts in a queue (or disconnects?) if no employees are available
        For now, we just give a message if call can't be handled and leave implementation for later
        """
        self._route_call(call)

    def _route_call(self, call)
        """ routes call to employee if any are available and returns success message (for now) """
        # see if any freshers are available
        if len(self._freshers) > 0:
            for e in self._freshers:
                if not e.is_busy:
                    e.receive_call(call)
                    return "success to fresher"
        elif len(self._tl_pm) > 0:
            for e in self._tl_pm:
                if not e.is_busy:
                    e.receive_call(call)
                    return "success to TL/PM"
        else:
            raise Exception("No employee is available to receive call")


class Call(object):
    def __init__(self):
        self.rank = 0  # min rank of employee that can handle this call. This is instance specific as it allows you to extend this class in the future if calls are tied to specific min ranks

    def reply(self, message):
        raise NotImplementedError("reply with some message")

    def disconnect(self):
        raise NonImplementedError("disconnect call")


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


class Fresher(Employee):
    def __init__(self):
        super(Fresher, self).__init__()  # initialize parent's properties/attributes in child
        self.rank = 0


class TL(Employee):
    def __init__(self):
        super(TL, self).__init__()  # initialize parent's properties/attributes in child
        self.rank = 1


class PM(Employee):
    def __init__(self):
        super(PM, self).__init__()  # initialize parent's properties/attributes in child
        self.rank = 2

mytl = TL()
print mytl.get_rank()
print mytl.is_busy()
mytl.receive_call("hello")
print mytl.is_busy()