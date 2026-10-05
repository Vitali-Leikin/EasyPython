# Задача №1
#
# Дан список:
ll1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
# необходимо вывести сумму элементов.
#

result = 0

for i in ll1:
    for j in i:
        result += j
print(result)


#
# Задача №2
#
# Дан список:
ll2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
# необходимо вывести максимальное значение.
#
max_item = ll2[0][0]

for i in ll2:
    for j in i:
        if j > max_item:
            max_item = j

print(max_item)

second_max_item = max(ll2)
print(max(second_max_item))

# Задача №3
#
# Дан список:
ll3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
# необходимо вывести количество элементов.

counter = 0
for i in ll3:
    for j in i:
        counter += 1

print(counter)
print(sum(len(el) for el in ll3))