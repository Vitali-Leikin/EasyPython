# def check_python(text):
#     # 1. Сохраняем очищенную строку в переменную
#     clean_text = text.strip().lower()
#
#     # 2. Проверяем наличие подстроки через in без цикла
#     if "python" in clean_text:
#         return True
#     else:
#         return False
#
import numbers


# def update_list(items):
#      items.append("финиш")
#      items.pop(0)
#      return items


# Задание 2: Фильтрация списка слов
# Напишите функцию get_cats(words), которая:
#
# Принимает список строк words (например, ["Кот", "собака", "КОТ", "мышь"]).
#
# Создаёт новый пустой список.
#
# Проходит циклом по переданному списку и добавляет в новый список только те слова, которые равны "кот" (без учёта регистра, то есть и "Кот", и "КОТ", и "кот").
#
# Возвращает получившийся список.

# def get_cats(words):
#     new_list = []
#     for word in words:
#         if word.lower()== "кот":
#             new_list.append(word)
#     return new_list
# print(get_cats(["Кот", "собака", "КОТ", "мышь"]))

# Задание 4: Функция sum_even_indices(numbers) — считаем сумму элементов, стоящих на чётных индексах (0, 2, 4...).
# Задание 4: Перебор списка по индексам
# Напишите функцию sum_even_indices(numbers), которая:
#
# Принимает список чисел numbers.
#
# Используя цикл по индексам (for i in range(len(numbers)):), считает сумму элементов, которые стоят только на чётных индексах (0, 2, 4 и т.д.). Подсказка: проверка на чётность индекса — if i % 2 == 0:.
#
# Возвращает посчитанную сумму.
#
# Подсказка: цикл по индексам for i in range(len(numbers)): и проверка if i % 2 == 0:.


# def sum_even_indices(numbers):
#     total = 0
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             total = total + numbers[i]
#     return total
# print(sum_even_indices([10,12,40,60,3]))

# Задание 5: Подсчёт подходящих элементов
# Напишите функцию count_long_words(words), которая:
#
# Принимает список строк words.
#
# Считает количество слов, длина которых строго больше 4 символов.
#
# Возвращает это итоговое число.

def count_long_words(words):
    count = 0
    for word in words:
        if len(word) > 4:
            count = count + 1
    return count
print(count_long_words(["hello", "world", "world", "world"]))