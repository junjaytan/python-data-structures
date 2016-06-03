

# allow multiple arguments to a function
def manyargs(*arg):
    for value in arg:
        print value

manyargs("hello", "there")

# comparisons via values
x = 5
y = 6
if x < y:
    print "x is less than y!"
elif x == y:
    print "x is equal to y!"
elif x > y:
    print "x is greater than y!"

if x != y:
    print "x is not equal to y!"

# comparison via object identity (i.e., not based on value, but whether it's the same object
x = 5
v = 5
z = x
if x == v:
    print "x is same value as v!"

if x is v:
    print "x is the same object as v!"

if z is x:
    print "z is the same object as x!"


# formatting output
# see: http://www.python-course.eu/python3_formatted_output.php