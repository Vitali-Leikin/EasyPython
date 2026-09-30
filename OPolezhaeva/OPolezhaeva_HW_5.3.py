# Задача №1
#
# Необходимо написать 4 функции:
# сложение 2х чисел
# вычитание 2х чисел
# умножение 2х чисел
# деление 2х чисел

# 1. Функция сложения

a = 1
b = 6

def add(a, b):
    return a + b
print("Сложение a и b =", add(a,b))

# 2. Функция вычитания

c = 7
d = 9

def subtract(c, d):
    return c - d
print("Разница c и d = ", subtract(c, d))

# 3. Функция умножения

e = 5
f = 9

def multiply(e,f):
    return e * f
print("Умножение e на f = ", multiply(e,f))

# 4. Функция деления

g = 9
h = 1

def divide(g,h):
    if h == 0:
        return "деление на ноль невозможно"
    return g / h
print("Деление g на h =", divide(g,h))

# Задачи №2
#
# https://www.codewars.com/kata/53ee5429ba190077850011d4/train/python

i =7

def double(i):
    return i * 2

print(double(i))

# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

flower1 = 2
flower2 = 8

def is_love(flower1, flower2):
    return flower1 % 2 != flower2 % 2

if is_love(flower1, flower2):
    print("Это любовь")
else: print("Не любовь")

# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python

i = 999,99

def transform(i):
    return str(i)

print(transform(i))

# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python

l = [34, -345, -1, 100]

def smallest_integer(l):
    return min(l)

print(smallest_integer(l))

# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python

n = 9

def count_sheep(n):
    result = ""
    for i in range(1, n + 1):
        result += f"{i} sheep \n"
    return result

print(count_sheep(n))
