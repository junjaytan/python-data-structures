def product_of_all_except_index_v1(a):
    """
    Uses 2 additional lists to calculate result. A better algorithm is v2, which only uses 1 additional array
    :param a: list of integers
    :return: list of integers representing the product of all other values except for the value at index
    """
    size = len(a)

    # trivial case
    if size <= 1:
        return a

    # initialize empty lists to hold products growing front to back and vice versa. These will be used to
    # calculate the product at each index in O(n) time
    a_products_front_to_back = [None] * size
    a_products_back_to_front = [None] * size
    a_output = [None] * size

    # fill in products that grow from front to back
    current_product = a[0]
    for index, element in enumerate(a):
        if index == 0:
            a_products_front_to_back[index] = current_product
            continue
        current_product = a[index] * current_product            # update current product
        a_products_front_to_back[index] = current_product       # set element equal to current product
    print "a front to back: " + str(a_products_front_to_back)

    # fill in products that grow from back to front
    current_product = a[size-1]
    for index in range(size-1, -1, -1):       #  if step is negative, the last element is the smallest int greater than stop
        if index == size-1:
            a_products_back_to_front[index] = current_product
            continue
        current_product = a[index] * current_product
        a_products_back_to_front[index] = current_product
    print "a back to front: " + str(a_products_back_to_front)

    # now calculate product of all other values but the index element's value at each index
    for index in range(0, size):
        # boundary conditions of first and last element
        if index == 0:
            a_output[index] = a_products_back_to_front[index+1]
        elif index == (size-1):
            a_output[index] = a_products_front_to_back[index-1]
        else:
            a_output[index] = a_products_front_to_back[index-1] * a_products_back_to_front[index+1]

    return a_output

def product_of_all_except_index_v2(a):
    """
    Uses 1 additional list to calculate result.
    Therefore runs in O(n) time and O(n) space
    :param a: list of integers
    :return: list of integers representing the product of all other values except for the value at index
    """
    size = len(a)

    # trivial case
    if size <= 1:
        return a

    # initialize empty lists to hold products growing front to back and vice versa. These will be used to
    # calculate the product at each index in O(n) time
    a_products_front_to_back = [None] * size
    a_output = [None] * size

    # fill in products that grow from front to back
    current_product = a[0]
    for index, element in enumerate(a):
        if index == 0:
            a_products_front_to_back[index] = current_product
            continue
        current_product = a[index] * current_product            # update current product
        a_products_front_to_back[index] = current_product       # set element equal to current product
    print "a front to back: " + str(a_products_front_to_back)

    # now fill in values using the front_to_back products, iterating from back to front through the input list
    # now calculate product of all other values but the index element's value at each index
    current_product_back_to_front = a[size-1]
    for index in range(size-1, -1, -1):
        # boundary conditions of first and last element
        if index == 0:
            a_output[index] = current_product_back_to_front
        elif index == (size-1):
            a_output[index] = a_products_front_to_back[index-1]
        else:
            a_output[index] = a_products_front_to_back[index-1] * current_product_back_to_front
            current_product_back_to_front = current_product_back_to_front * a[index]

    return a_output


if __name__ == "__main__":
    a = [2, 3, 3, 5]
    #a = []
    print product_of_all_except_index_v2(a)
