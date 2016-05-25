
def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]

        i = j-1
        while i>=0 and a[i] > key:  # note: python loop termination index is different from CLRS
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
    return a

if __name__ == "__main__":
    test_list = [1, 3, 4, 0, 9, 2, 11]

    b = insertion_sort(test_list)
    print b

    alpha = ['a', 'bb', 'zz', 'y', 'c']
    c = insertion_sort(alpha)
    print c


