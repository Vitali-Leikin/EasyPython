import re
def sum_of_elms(array: list) -> float:
    return sum(sum(i) for i in array)


def max_elm(array: list) -> float:
    return max(max(i) for i in array)


def quantity_of_elms(array:list) -> int:
    return sum(len(i) for i in array)


def left_matrix():
    k = 11
    for i in range(10):
        k -= 1
        for j in range(k):
            print(j, end=" ")
        print()


def right_matrix():
    k = 11
    m = 0
    for i in range(10):
        print(" " * m, end=" ")
        k -= 1
        m += 2
        for j in range(0, k):
            print(j, end=" ")
        print()


def full_matrix():
    k = 11
    m = 0
    for i in range(10):
        k -= 1
        print(" " * m, end=" ")
        m += 2
        for j in range(k-1, 0, -1):
            print(j, end=" ")
        for j in range(k):
            print(j, end=" ")
        print()


def return_all_o(text: str) -> str:
    return "".join(ch for ch in text if ch == "о")


def count_e(text: str) -> int:
    return text.count("е")


def quantity_words_without_e(array: list) -> int:
    return sum(1 for i in array for j in i if "е" not in j)

def return_start_index(text: str) -> list:
    """
    :param text: строка “Посмотрите как Рите нравится ритм”
    :return: Вернет индексы начала всех подстрок - “рит”, независимо от регистра
    """
    return [i.start() for i in re.finditer(r"рит", text, flags=re.IGNORECASE)]
