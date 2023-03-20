# value as last element of my_list
def add(my_list, value):
    my_list.append(value)


def test_add():
    l = [1, 2, 3]
    add(l, 4)
    assert l == [1, 2, 3, 4]

    add(l, 10)
    assert l == [1, 2, 3, 4, 10]

    add(l, -2)
    assert l == [1, 2, 3, 4, 10, -2]


# insert number value at index
def insert(my_list, index, value):
    if (-1 < index <= len(my_list)):
        my_list.insert(index, value)
    else:
        print("index error")


def test_insert():
    l = [1, 2, 3]

    insert(l, 2, 12)
    assert l == [1, 2, 12, 3]

    insert(l, -1, 4)
    assert l == [1, 2, 12, 3]

    insert(l, 14, 3)
    assert l == [1, 2, 12, 3]


# removes the element at index
def remove(my_list, index):
    if (-1 < index < len(my_list)):
        my_list.pop(index)


def test_remove():
    l = [1, 2, 3]

    remove(l, -1)
    assert l == [1, 2, 3]

    remove(l, 0)
    assert l == [2, 3]

    remove(l, 10)
    assert l == [2, 3]


# removes elements between the two given index
def remove_interval(my_list, from_index, to_index):  # not working
    nr = to_index - from_index + 1
    if -1 < from_index < len(my_list) and -1 < to_index < len(my_list):

        if to_index < from_index:
            print("the interval is not well defined")
        else:
            while (nr != 0):
                my_list.pop(from_index)
                nr = nr - 1


def remove_elements(my_list, from_index, to_index):  # not working
    if -1 < from_index < len(my_list) and -1 < to_index < len(my_list):
        if to_index < from_index:
            print("the interval is not well defined")
        else:
            del my_list[from_index:to_index + 1]


# replaces all old_value occurances with new_value
def replace(my_list, old_value, new_value):
    for i in range(0, len(my_list)):
        if my_list[i] == old_value:
            my_list[i] = new_value


def test_replace():
    l = [1, 2, 3]

    replace(l, 1, 2)
    assert l == [2, 2, 3]

    replace(l, 0, 13)
    assert l == [2, 2, 3]

    replace(l, 2, 15)
    assert l == [15, 15, 3]


# verifies if a given number is prime
def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    elif n % 2 == 0:
        return False
    else:
        for d in range(3, n // 2, 2):
            if n % d == 0:
                return False
    return True


# get prime number between two given index (it could be more than one)
def prime(my_list, from_index, to_index):
    if from_index < 0 or from_index > len(my_list) - 1 or to_index < 0 or to_index > len(
            my_list) - 1 or from_index > to_index:
        print("index error")
    else:
        for i in range(from_index, to_index + 1):
            if is_prime(my_list[i]) == True:
                print(my_list[i])


def test_prime():
    l = [1, 2, 3]
    assert prime(l, 0, 2) == (2, 3)

    l = [-2, 0, 4]
    assert prime(l, 1, 2) == ()

    l = [5, 7, 13]
    assert prime(l, 0, 1) == (5, 7)


# get odd number between the two given index (it could be more than one)
def odd(my_list, from_index, to_index):
    if from_index < 0 or from_index > len(my_list) - 1 or to_index < 0 or to_index > len(
            my_list) - 1 or from_index > to_index:
        print("index error")
    else:
        for i in range(from_index, to_index + 1):
            if my_list[i] % 2 == 1:
                print(my_list[i])


def test_odd():
    l = [1, 2, 3]
    assert odd(l, 0, 2) == (1, 3)

    l = [2, 4]
    assert odd(l, 0, 1) == ()

    l = [1, 3, 5, 7]
    assert odd(l, 2, 3) == (5, 7)


# get sum of elements between the two given index
def sequence_sum(my_list, from_index, to_index):
    if from_index < 0 or from_index > len(my_list) - 1 or to_index < 0 or to_index > len(
            my_list) - 1 or from_index > to_index:
        print("index error")
    else:
        s = 0
        for i in range(from_index, to_index + 1):
            s += my_list[i]
    print(s)


def test_sequence_sum():
    l = [1, 2, 3]
    assert sequence_sum(l, 0, 2) == 6

    l = [1, 2, 3, 3, 3, 5]
    assert sequence_sum(l, 3, 4) == 6

    l = [2, 4, 5, 6]
    assert sequence_sum(l, 0, 1) == 6


# get the gcd of a and b
def euclid(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while b > 0:
            r = a % b
            a = b
            b = r
    return a


# get the greatest common divisor of elements between the two given index
def sequence_gcd(my_list, from_index, to_index):
    if from_index < 0 or from_index > len(my_list) - 1 or to_index < 0 or to_index > len(
            my_list) - 1 or from_index > to_index:
        print("index error")
    else:
        var = euclid(my_list[from_index], my_list[from_index + 1])
        for i in range(from_index + 2, to_index + 1):
            var = euclid(var, my_list[i])
    print(var)


def test_sequence_gcd():
    l = [1, 2, 3]
    assert sequence_gcd(l, 0, 2) == 1

    l = [16, 24, 48]
    assert sequence_gcd(l, 0, 1) == 8

    l = [73, 27]
    assert sequence_gcd(l, 0, 1) == 1


# get maximum of elements between the two given index
def sequence_max(my_list, from_index, to_index):
    if from_index < 0 or from_index > len(my_list) - 1 or to_index < 0 or to_index > len(
            my_list) - 1 or from_index > to_index:
        print("index error")
    else:
        max = my_list[from_index]
        for i in range(from_index, to_index + 1):
            if my_list[i] > max:
                max = my_list[i]
    print(max)


def test_sequence_max():
    l = [1, 2, 3]
    assert sequence_max(l, 0, 2) == 3

    l = [43, 2, 3, 59, 2]
    assert sequence_max(l, 2, 4) == 59

    l = [1, 1, 1, 1]
    assert sequence_max(l, 1, 2) == 1


# keep only prime numbers, remove other elements
def filter_prime(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        if is_prime(my_list[i]) == False:
            remove(my_list, i)


def test_filter_prime():
    l = [1, 2, 3, 4, 5]
    filter_prime(l)
    assert l == [2, 3, 5]

    l = [1, 14, 14, 8, 9]
    filter_prime(l)
    assert l == []

    l = [3, 5, 7]
    filter_prime(l)
    assert l == [3, 5, 7]


# keep only the negative numbers, remove other elements
def filter_negative(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] >= 0:
            remove(my_list, i)


def test_filter_negative():
    l = [1, 2, 3]

    filter_negative(l)
    assert l == []

    l = [-1, 3, -5]
    filter_negative(l)
    assert l == [-1, -5]

    l = [-1, -2]
    filter_negative(l)
    assert l == [-1, -2]
