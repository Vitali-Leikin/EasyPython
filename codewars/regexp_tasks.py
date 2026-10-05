import re

def task_1(text: str) -> list:
    """
    :param text: строка
    :return: список всех чисел в строке, каждый элемент списка строка
    """
    return re.findall(r"\d+", text)


def task_2(code: str) -> bool:
    """
    :param code: строка
    :return: Выведет True если строка подходит под шаблон две заглавные буквы, затем две цифры, иначе False
    """
    return bool(re.fullmatch(r"[A-Z]{2}\d{2}", code))


def task_3(text: str) -> str:
    """
    :param text: строка
    :return: строку в которой все цифры заменены на символ #
    """
    return re.sub(r"\d", "#", text)

def task_4(text: str) -> list:
    """
    :param text: строка "aa bb ac ba"
    :return: список строк состоящих только из букв a или b, ['aa', 'bb', 'ba']
    """
    return re.findall(r"\b[ab]+\b", text)


def task_5(text: str) -> bool:
    """
    :param text: строка "Python это круто!"
    :return: True если строка начинается со слова "Python" и заканчивается "!", иначе False
    """
    return bool(re.search(r"^Python.*!$", text))


def task_6(text: str) -> list:
    """
    :param text: строка "cat concatenate cat."
    :return: список всех вхождений слова "cat" как отдельного слова
    """
    return re.findall(r"\bcat\b", text)


def task_7(text: str) -> list:
    """

    :param text: строка
    :return: список слов, которые начинаются с Python
    """
    return re.findall(r"\bPython\w*", text)


def task_8(text: str) -> bool:
    """
    :param text: строка
    :return: True если в строке есть отдельное слово "рублей", иначе False
    """
    return bool(re.search(r"\bрублей\b", text))

def task_9(text: str) -> list:
    """
    :param text: строка
    :return: список всех 'abc' которые являются отдельным словом
    """
    return re.findall(r"\babc\b", text)

def task_10(text: str) -> str:
    """
    :param text: строка "кот котёнок кот."
    :return: строку в которой отдельное слово 'кот' замено на 'пес'
    """
    return re.sub(r"\bкот\b", "пес", text)

