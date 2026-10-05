# Задача №1
#
# Необходимо написать 4 функции:
# сложение 2х чисел
# вычитание 2х чисел
# умножение 2х чисел
# деление 2х чисел

# сложение 2х чисел
def summ (num1, num2):
    return num1 + num2
print(summ(1, 2))


# вычитание 2х чисел
def deduct (num1, num2):
    return num1 - num2
print(deduct(1, 2))

# умножение 2х чисел
def  multiply (num1, num2):
    return num1 * num2
print(multiply(6, 2))

# деление 2х чисел
def divide (num1, num2):
    return num1 / num2
print(divide(10, 2))

# Задачи №2

# https://www.codewars.com/kata/53ee5429ba190077850011d4/train/python
# Need to double the integer and return it.

def double_integer(i):
    return i * 2

# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
# Тимми и Сара думают, что влюблены, но в их краях это можно узнать, лишь сорвав по цветку. Если у одного цветка четное количество лепестков, а у другого — нечетное, значит, они влюблены.
# Напишите функцию, которая принимает количество лепестков каждого цветка и возвращает `true`, если они влюблены, и `false`, если нет.
def lovefunc( flower1, flower2 ):
    total = flower1 + flower2
    if total % 2 == 0:
        return False
    else:
        return True
print(lovefunc(2, 2))

# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
# We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    text = str(num)
    return text
print(number_to_string(10))

# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
# Given an array of integers your solution should find the smallest integer.
def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return (smallest)

# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    sheep = ""
    for i in range(1, n + 1):
        sheep += f"{i + 1} sheep..."
    return sheep
print(count_sheep(3))