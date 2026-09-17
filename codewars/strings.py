def get_count(sentence: str):
    """
    Считает кол-во гласных букв (a, e, i, o, u) в строке
    :param sentence: строка в которой нужно посчитать гласные
    :return: количество гласных букв a, e, i, o, u входящих в sentence
    """
    count = 0
    for ch in sentence:
        if ch in "aeiou":
            count += 1
    return count


def remove_vowels(text: str) -> str:
    """
    Удаляет гласные из строки
    :param text: строка из которой надо убрать гласные
    :return: строку без гласных
    """
    return "".join(ch for ch in text if ch not in "aeiou")


def no_repeat(text: str) -> str | None:
    '''Возвращает первый символ, который встречается в строке только один раз
    :param text: строка в которой нужно найти уникальный символ
    :return: первый символ, встречающийся в строке только один раз
    '''
    for ch in text:
        if text.count(ch) == 1:
            return ch
    return None


def spacey(array: list) -> list:
    """
    Убирает пробелы между словами, последовательно склеивая элементы массива
    :param array: список строк ['i', 'have', 'no', 'space']
    :return: список из склееных слов ['i', 'ihave', 'ihaveno', 'ihavenospace']
    """
    k = []
    s = ''
    for i in array:
        s += i
        k.append(s)
    return k
