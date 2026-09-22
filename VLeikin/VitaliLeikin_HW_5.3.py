# Задача №1
#
# Необходимо написать 4 функции:
# сложение 2х чисел
# вычитание 2х чисел
# умножение 2х чисел
# деление 2х чисел

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Ошибка: деление на ноль!"

def calculate_dict(a, b, sign):
    try:
        num1 = float(a)
        num2 = float(b)
    except (ValueError, TypeError):
        return "Ошибка: можно использовать только числа!"

    match sign:
        case "+":
            return  add(num1, num2)
        case "-":
            return  sub(num1, num2)
        case "*":
            return mul(num1, num2)
        case "/":
            return div(num1, num2)
        case _:
            return f"Ошибка: неизвестный знак операции '{sign}'"

print(calculate_dict(2,3,"+"))
print(calculate_dict(4,3,"-"))
print(calculate_dict(2,3,"*"))
print(calculate_dict(2,3,"/"))
print(calculate_dict(2,0,"/"))
print(calculate_dict(2,3,"^"))
