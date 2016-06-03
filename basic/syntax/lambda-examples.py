# http://www.secnetix.de/olli/Python/lambda_functions.hawk

"""
One use of lambdas is to sort instances of a class by an attribute
"""
def lambdas_class_example():
    class Meeting(object):
        def __init__(self, starttime, endtime):
            self.starttime = starttime
            self.endtime = endtime

        def to_string(self):
            return "(%f, %f)" % (self.starttime, self.endtime)

    mymeetings = [Meeting(9, 12), Meeting(3, 5), Meeting(6, 7), Meeting(3, 9), Meeting(12, 15), Meeting(15.5, 17)]

    sorted_meetings = sorted(mymeetings, key= lambda meeting: meeting.starttime)
    for element in sorted_meetings:
        print element.to_string()

"""
Another use of lambdas is to create an incrementor function
"""
def lambda_incrementor_example():
    def make_incrementor(n):
        return lambda x: x + n

    f = make_incrementor(1)
    print f(2)  # increment f by this value
    print f(4)  # increment f by this value
    print make_incrementor(1)(4)
    # print make_incrementor(1)(3)(4)   # raises exception

"""
map(function, iterable) applies a function to every item of the iterable and returns a list of results
it is commonly used with lambdas
"""
def lambda_map_example():
    mylist = [1, 3, 4]
    print "orig list: " + str(mylist)

    mylist2 = map(lambda x: x * 3, mylist)
    print "list after applying lambda: " + str(mylist2)

if __name__ == "__main__":
    #lambdas_class_example()
    #lambda_incrementor_example()
    lambda_map_example()