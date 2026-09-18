def odd_numbers(array: list) -> list:
    return [i for i in array if i % 2 == 0]


def more_than_5(array: list) -> list:
    return [i for i in array if i > 5]


def multiply_15(array: list) -> list:
    return [i * 15 for i in array]


def sum_numbers(array: list):
    k = 0
    for i in array:
        k += i
    return k


def max_value(array: list):
    m = array[0]
    for i in array:
        if i > m:
            m = i
    return m


def min_value(array: list):
    m = array[0]
    for i in array:
        if i < m:
            m = i
    return m


def mean(array: list):
    return f"{sum(array) / len(array):.3f}"


def sum_two_num(a, b):
    return a + b


def sub_two_num(a, b):
    return a - b


def multiply_two_num(a, b):
    return a - b


def div_two_num(a, b):
    return f"{a / b:.3f}"

""" codewars """


def double_integer(i):
    return i * 2


def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2


def number_to_string(num):
    return str(num)


def find_smallest_int(arr):
    k = arr[0]
    for i in arr:
        if i < k:
            k = i
    return k


def count_sheep(n):
    str = ""
    for i in range(n):
        str += f"{i + 1} sheep..."
    return str

