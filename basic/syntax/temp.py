
# allow multiple arguments to a function
def manyargs(*arg):
    for value in arg:
        print value

manyargs("hello", "there")