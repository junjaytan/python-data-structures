def fib_n_recurse(n):
    """ recursive method of calculating nth fibonacci number """
    if n <= 2:
        return 1
    else:
        return fib_n_recurse(n-1) + fib_n_recurse(n-2)

def fib_n_dp1(n):
    """ calculate fibonacci number using dp list that grows """
    fib_values = [0, 1]
    for i in range(2, n+1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    return fib_values(n)

def fib_n_dp2(n):
    """ even better, calculate fibonacci number using only 2 additional variables """
    i = 3
    prev_value = 1
    prev_prev_value = 1
    if n <= 2:
        return 1
    for i in range(3, n+1):     # need to increment to n+1 because range only goes up to value before n+1
        new_value = prev_prev_value + prev_value

        prev_prev_value = prev_value
        prev_value = new_value

    return new_value



if __name__ == "__main__":
    #print fib_n_recurse(30)

    print fib_n_dp2(100)