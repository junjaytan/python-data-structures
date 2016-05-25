
# Polynomial hash code
def polynomial_hash_code(s):
    """ Use a polynomial in a (a != 1) which converts a object (in tuple form) to has code """
    raise NotImplementedError('not implemented yet')

def cyclic_shift_hash_code(s):
    """ Use a cyclic shift of a partial sum by a certain number of bits
    Uses Python bitwise operators """
    mask = (1 << 32) -1                     # limit to 32-bit integer
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)     # 5-bit cyclic shift in r
        h += ord(character)                 # add in value of next ch
    return h

# Python also has a built-in hash(x) function that returns an integer value.
# However, it only works on immutable data types (int, float, str, tuple, frozenset)