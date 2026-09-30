# region Task 1
# Необходимо создать целочисленные переменные a и b, присвоить произвольные значения переменным
# на ваш выбор и вывести результаты следующих операций с этими переменными: сложение, умножение,
# вычитание, деление и остаток от деления. Также сделать проверку на четность этих переменных и
# вывести результат.

# a = 5
# b = 10

# print(res1 := a+b)
# print(res2 := a*b)
# print(res3 := a-b)
# print(res4 := a/b)
# print(res5 :=a%b)

# if res1 % 2 == 0:
#     print(res1, 'even')
# else:
#     print(res1, 'not even')

# if res2 % 2 == 0:
#     print(res2, 'even')
# else:
#     print(res2, 'net even')

# if res3 % 2 == 0:
#     print(res3, 'even')
# else:
#     print(res3, 'not even')

# if res4 % 2 == 0:
#     print(res4, 'even')
# else:
#     print(res4, 'not even')

# if res5 % 2 == 0:
#     print(res5, 'even')
# else:
#     print(res5, 'not even')

# endregion

#region Task 2
# Необходимо создать целочисленные переменные a и b, присвоить им произвольные значения,
# а потом поменять значения местами (значение переменной a должно оказаться в переменной b и наоборот).

# a = 5
# b = 10

# a, b = b, a

# print(a, b)

# endregion

# region Task 3
# Создать программу дележа добычи на пиратском корабле. По обычаю, половина добычи идет
# владельцу корабля, половина оставшегося — капитану, остальное делится поровну между
# всеми членами команды, включая капитана.

# Размер добычи (например, в дублонах) и количество пиратов на корабле задать переменными.

# Вывести на экран кому сколько дублонов полагается
# Сколько получит капитан (Джек Воробей, естественно), если он утверждает,
# что корабль принадлежит ему?

# pirates = 5
# fullAmount = 10000

# ownerSum = fullAmount / 2
# captainSum = (fullAmount - ownerSum) / 2
# otherSum = (fullAmount - ownerSum - captainSum) / (pirates + 1)
# totalCaptainSum = captainSum + otherSum
# ownerIsCaptain = ownerSum + totalCaptainSum

# print(f"Владельцу корабля полагается {ownerSum} дублонов. Капитану (если он не владелец) - {totalCaptainSum} дублонов. Обычным пиратам - {otherSum} дублонов каждому. Если капитан владелец корабля, то ему полагается - {ownerIsCaptain} дублонов")