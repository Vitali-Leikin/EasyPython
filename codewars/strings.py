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

def change_letter(text: str) -> str:
    '''
    Заменяет буквы на их номер в алфавите, не буквенные символы оставляет как есть
    :param text: строка
    :return: строка с замененными буквами
    '''

    return "".join(str(ord(ch) - 96) if "a" <= ch.lower() <= "z" else ch for ch in text)

def greet_jedi(first: str, last: str) -> str:
    """
    Строку сформированную по шаблону: первые три буквы фамилии + первые две буквы имени
    оба параметра приводятся к виду "Заглавная + строчные"
    :param first: имя, беруться два первых символа
    :param last: фамилия, берутся три первых символа
    :return: строка вида <3 буквы фамилии> <2 буквы имени>
    """
    return last[0:3].capitalize() + first[0:2].capitalize()

def start_with_a(text: str) -> str:
    """
    Отфильровывает строку, оставляя в ней только слова начинающиеся на букву "а", с учетом регистра
    :param text: строка из любых символов и букв
    :return: строку состоящую из слов начинающихся на "а"
    """
    return " ".join(w for w in text.split() if w.startswith("а"))

def numbers_more_than_zero(n: int) -> bool:
    """
    Проверяет, что все цифры передаваемого числа больше нуля
    :param n: целое число
    :return: Возвращает True если все цифры числа > 0: иначе False
    """
    return all(int(i) > 0 for i in str(abs(n)))