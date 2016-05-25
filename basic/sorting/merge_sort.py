# top down merge sort
# O(n log n) time (worse/expected)
def merge_sort(s):      # s is a list of elements
    """

    :param s:
    :return:
    """
    if len(s) == 1:
        return s
    else:
        midpoint = len(s) // 2
        l = merge_sort(s[0:midpoint])
        r = merge_sort(s[midpoint:len(s)])
        return merge(l, r)


def merge(l, r):
    # merges 2 subarrays into one subarray, ordered based on comparing top element in l to top element in r
    # due to recursion, your inputs to merge will eventually be two ordered subarrays
    l.append(None)  # append sentinel
    r.append(None)  # append sentinel
    merged = []

    i = 0
    j = 0
    while (l[i] is not None) and (r[j] is not None):
        if l[i] < r[j]:
            print "index, value are: %s, %s" % (str(i), str(l[i]))
            merged.append(l[i])
            i += 1

        else:
            print "index, value are: %s, %s" % (str(j), str(r[j]))
            merged.append(r[j])
            j += 1

    if l[i] is None:
        while r[j] is not None:
            merged.append(r[j])
            j += 1
    elif r[j] is None:
        while l[i] is not None:
            merged.append(l[i])
            i += 1
    return merged

if __name__ == "__main__":
    a = [1, 4, 2, 5, -1, 0]
    b = [3, 2, 0]
    print merge_sort(a)