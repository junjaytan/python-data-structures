'''
see:
http://stackoverflow.com/questions/13142041/build-a-max-heap-and-iteration
'''

def max_heapify(A, i):
    left = (2 * i) + 1  # or 2i?
    right = (2 * i) + 2 # or 2i + 1?
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
        


if __name__ == "__main__":
    print "hello world"