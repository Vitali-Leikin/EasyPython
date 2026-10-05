"""Задача №1"""

s = 'Перестановочный алгоритм быстрого действия'

for letter in s:
    if letter == 'о':
        print(letter)
print(s)


"""Задача №2"""

s = 'Перевыборы выбранного президента'

count = 0

for letter in s:
    if letter == 'е':
        count += 1
print(count)


"""Задача №3"""

s = 'Посмотрите как Рите нравится ритм'

count = 0

low = s.lower()

for i in range(len(low)):
    if low[i:i + 3] == 'рит':
        print(i)


"""Задача №4"""

ll = [['Привет', 'всем', 'кто'], ['изучает', 'язык', 'программирования'], ['java']]

count = 0

for i in ll:
    for j in i:
        if 'е' in j:
            break
    else:
        count += 1
print(count)