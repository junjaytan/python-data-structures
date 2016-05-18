
# 1.2: Reverse string
def reverse_str(s):
    orig = list(s)
    size = len(orig)

    for i in range(0, size/2):
        orig[i], orig[size-1-i] = orig[size-1-i], orig[i]

    return ''.join(orig)

mystring = 'hello232 dfaa'
reversed = reverse_str(mystring)
print reversed