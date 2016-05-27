from operator import mul

def highest_prod_three_ints(a):
    """
    :param a: list of integers
    :return: highest product of three integers

    The array could have both positive and negative integers
        if size < 3: raise exception
        if size == 3: trivial case
        if all positive numbers, then largest product is product of 3 largest integers
        if positive and negative, largest product could be:
            product of 3 largest positive integers, or
            product of 2 smallest neg integers * largest positive integer

    use an array to keep track of the 2 smallest neg integers, and an array to keep track of the 3 largest pos integers
    """

    smallest_neg = []
    largest_pos = []

    # trivial cases
    if len(a) < 3:
        return None
    if len(a) == 3:
        return reduce(mul, a)

    # now bucket array values into pos and neg values

    # initialize some vars used in comparisons
    second_smallest_neg = 0
    smallest_pos = 0

    for element in a:
        if (element < 0 and element < second_smallest_neg) or len(smallest_neg) < 2:
            if len(smallest_neg) == 2:                          # if list is at capacity, remove largest item
                smallest_neg.remove(max(smallest_neg))
            smallest_neg.append(element)
            second_smallest_neg = max(smallest_neg)
        elif (element > 0 and element > smallest_pos) or len(largest_pos) < 3 :
            if len(largest_pos) == 3:
                largest_pos.remove(min(largest_pos))            # if list is at capacity, remove smallest item
            largest_pos.append(element)
            smallest_pos = min(largest_pos)

    # now sort our lists so we can refer to them appropriately
    smallest_neg.sort()
    largest_pos.sort()

    print smallest_neg
    print largest_pos

    if len(smallest_neg) <= 1:                                   # if no negative values, or only one neg value
        return reduce(mul, largest_pos)                         # then largest prod is from multiplying largest pos values
    elif len(largest_pos) < 3:                                  # edge case of only 2 positive values
        return 0
    else:
        # return max of either 2 smallest negs x largest positive, or largest positives
        two_negs_one_pos = []
        two_negs_one_pos.extend(smallest_neg)
        two_negs_one_pos.append(largest_pos[2])

        return max(reduce(mul, two_negs_one_pos), reduce(mul, largest_pos))
        return True


if __name__ == "__main__":
    a = [-10, -7, 1, 3, 5, 6, 0, 11, 12, 15]
    prod = highest_prod_three_ints(a)
    print prod








