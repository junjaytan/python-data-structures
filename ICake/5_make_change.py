# see: http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/


# assume you always have at minimum 1cent denomination
def make_change_recursive(amount, denominations):
    # can solve recursively, by categorizing into solutions that contain mth coin, and solutions that don't contain mth coin
    # assumes denominations are already sorted smallest to largest
    # starting with largest count, pick 1 or more until

    # trivial edge cases
    if amount < 0 or len(denominations) == 0:
        return 0
    elif amount == 0:
        # if remaining amount is zero, it means either you've already been able to make change with largest denomination
        # or you can return change as empty set, so still 1 way
        return 1


    if len(denominations) == 1:  # if only one type of coin left
        if amount % denominations[0] == 0:
            return 1  # and it can make change for the remaining amount, return 1
        else:
            return 0  # else can't make change
    else:
        print denominations
        denominations_one_less = denominations[0:len(denominations)-1]
        return make_change_recursive(amount, denominations_one_less) + make_change_recursive(amount - denominations[-1],denominations)


def make_change_dp(amount, denominations):
    """ More efficient way is to use dynamic programming"""


if __name__ == "__main__":
    amount = 5
    denominations = [3, 3]

    # ensure denominations are sorted from smallest to largest
    denominations.sort()            # timsort worst: O(n log n)

    num_ways = make_change_recursive(amount, denominations)
    print "num ways to make change: %d" % num_ways