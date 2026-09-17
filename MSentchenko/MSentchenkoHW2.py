
# Задача 1
a = 5
b = 2

y = a + b
x = a * b
c = a - b
d = a / b
e = a % b

print(y)
print(x)
print(c)
print(d)
print(e)

# Задача 2

a = 10
b = 2

a,b = b,a

print(a)
print(b)

# Задача 3

dublons = 200
commandPirate = 30
cpt = 1
allTeam = commandPirate + cpt

# # Вычилсяем сколько получает владелец корабля
shipOwner = dublons / 2
print('Владелец корабля', shipOwner)
# # Вычисляем сколько получает Капитан
moneyCpt = (dublons - shipOwner) / 2
print('Остаток денег капитану корабля после того как отдали владельцу', moneyCpt)
# # Вычисляем сколько получат остальные , капитан также учитывается
moneyTeam =  (dublons - shipOwner - moneyCpt) / allTeam
print('Каждый в команде получил', moneyTeam)
# # Вычисляем сколько получил капитан
allMoneyJack = shipOwner + moneyCpt + moneyTeam
print('Джек получил на руки', allMoneyJack)
# # Вычисляем сколько получил каждый пират
pirateMoney = (dublons - allMoneyJack) / commandPirate
print('Каждый пират получил на руки', pirateMoney)

