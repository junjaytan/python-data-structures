tup1 = ('physics', 'chemistry', 1997)

# empty tuple
tupempty = ()

# tuple with single value (comma is required!)
tupsingle = (50,)

print tupsingle[0]

# basic operations
print "tuple length"
print len(tup1)

print "tuple concat"
print tup1 + tupsingle

print "tuple membership"
print 1997 in tup1

print "tuple iteration"
for x in tup1: print x