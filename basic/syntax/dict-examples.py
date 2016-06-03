# Dictionaries are basically hashes


# initialize dictionary
# ...directly
mydict2 = {'john': 1, 'mary': 2}
print mydict2

# ...via the dict() constructor, which takes sequences of key-value pairs
mydict = dict([('john', 1), ('mary', 2)])
print mydict

# loop through key-value pairs in dictionary
print "looping through dictionary key value pairs"
for k,v in mydict.items():
    print (k, v)