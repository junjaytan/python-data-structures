
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


# ---1.4: determine if 2 strings are Anagrams
def is_anagram(s1, s2):
    """ Determine if strings s1 and s2 are anagrams of one another
    Return True or False"""
    # since strings are immutable, convert each one to a list
    s1list = list(s1.lower())       #     ignores casing
    s2list = list(s2.lower())

    # if you know lengths are different, they cannot be anagrams
    if len(s1list) != len(s2list):
        return False
    else:
        # sort both lists in place. Alternatively you can use sorted(list) but this returns a new list
        s1list.sort()
        s2list.sort()
        for i in range(0, len(s1)):
            if s1list[i] != s1list[i]:
                return False
        return True

s1 = "hello"
s2 = "oLlEh"

print is_anagram(s1, s2)


#---- 1.5: replace spaces with %20
def replace_space(s):
    slist = list(s)     # python strings are immutable, so convert to mutable list
    for i in range(0, len(slist)):      # O(n)
        if slist[i] == ' ':
            slist[i] = '%20'            # O(1)
    return ''.join(slist)

teststring1_5 = 'hello there yo'
print replace_space(teststring1_5)


#--- 1.7: zero all elements in row/col if there's a zero value
def zero_matrix_rowcol(m):      # m is a row list of col lists (matrix)
    # might want to handle null case

    # might want to first verify that matrix is indeed rectangular M x N
    if not validate_rec_matrix(m):
        raise Exception('Matrix is not rectangular')

    # initialize sets that will store indices of rows and cols to zero
    rows_to_zero = set()
    cols_to_zero = set()

    # loop through matrix and identify zero elements
    for row_index, row in enumerate(m):
        for col_index, col in enumerate(row):
            # if zero value is encountered, skip the rest of that row and column
            print "coord: %s, %s" % (str(row_index), str(col_index))
            print "value: %s" % str(col)
            if col == 0:
                rows_to_zero.add(row_index)
                cols_to_zero.add(col_index)

    # now zero rows and cols
    print rows_to_zero
    print cols_to_zero
    # ... to be completed


def validate_rec_matrix(m):
    size = len(m[0])    # all other col lengths should match this
    for i in range(1, len(m)):
        if len(m[i]) != size:
            return False
    return True

mymatrix = [[1, 3, 4, 5, 0], [2, 4, 5, 6, 10], [3, 1, 4, 5, 6]]
zero_matrix_rowcol(mymatrix)


#----- 1.8: determine if string1 and string2 are rotated versions of the same string
def is_rotated_string(s1, s2):

    # concatenate string s1 with itself and see if s2 is a substring
    if (len(s1)==len(s2)) and len(s1)>0:
        print "Determining if is rotation:"
        return substring_exists(s2, s1+s1)
    return False



def substring_exists(substr, s):
    # Note: is case sensitive
    if substr in s:
        return True
    else:
        return False

substr = 'yo'
str = 'helyo'

s1 = 'eappl'
s2 = 'apple'

print is_rotated_string(s1, s2)