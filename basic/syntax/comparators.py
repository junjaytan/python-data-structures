# comparisons via boolean

x = True

# if x is true, then something
if x:
    print "something"

# testing if a list is empty
a = []
b = [1, 2]
print "testing if a is empty via 'not a':"
print not a

print "testing if b is empty via 'not b':"
print not b


"""
'is' returns True if 2 variables point to the same object.
'==' returns True if 2 objects referred to by the variables are equal
"""

# for small integers, Python caches small integer objects so 'is' returns true whereas it does not hold for large integers
x = 1000
y = 1000
z = 10**3

print "z == x?"
print z == x

print "y == x?"
print y == x

print "y is x?"
print y is x

print "z is x?"
print z is x

print "x = 100?"
print x == 1000

print "x = 10**3?"
print x == 10**3


f = None
g = None
print "f is None?"
print f is None

print "f == None?"
print f == None

print "f is g?"
print f is g

print "f == g?"
print f == g

class MyTestClass(object):
    def __init__(self, word):
        self.word = word

aclass = MyTestClass("hi")
bclass = MyTestClass("hi")

print "aclass == bclass?"
print aclass.word == bclass.word

print "aclass is bclass?"
print aclass.word is bclass.word