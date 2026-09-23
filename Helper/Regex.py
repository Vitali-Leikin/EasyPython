from enum import Enum
import re


# Пример создания и использования регулярных выражений



class RegexPattern:
    """
    создаем класс с полями которые будем использовать для проверки
    """
    numeric_check = r"^\d+$"
    latin_letter_check = r"^[a-zA-Z'’\- ]+$"
    numbers_and_dashes_check = r"^[0-9-]*$"
    street_name_check = r"^[a-zA-Z0-9'\- ]+$"
    street_name_length_check = r"^.{2,56}$"
    uppercase_latin_and_numbers_check = r"^[A-Z0-9]+$"
    id_document_length_check = r"^.{9,18}$"
    name_check = r"^[a-zA-Z''\- ]+$"
    name_length_check = r"^.{1,50}$"
    phone_number_check = r"^\d{9,}$"
    city_name_check = r"^[a-zA-Z'\- ]+$"
    city_name_length_check = r"^.{1,168}$"
    email_format_check = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    email_domain_extension_check = r"^.+@.+\.[a-zA-Z]{2,}$"
    email_allowed_chars_check = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+$"


class ValidationType(Enum):
    """
        создаем класс Enum / перечеслиление для убодства дальнейщего использования,
        что бы вручную не вводить данные при вызове методов для этого используем библиотеку enum
        также используем библитеку re  для соотношения регулярных выражения с введенными данными
    """

    numeric = RegexPattern.numeric_check
    latin_letter = RegexPattern.latin_letter_check
    numbers_and_dashes = RegexPattern.numbers_and_dashes_check
    street_name = RegexPattern.street_name_check
    street_name_length = RegexPattern.street_name_length_check
    uppercase_latin_and_numbers = RegexPattern.uppercase_latin_and_numbers_check
    id_document_length = RegexPattern.id_document_length_check
    name = RegexPattern.name_check
    name_length = RegexPattern.name_length_check
    phone_number = RegexPattern.phone_number_check
    city_name = RegexPattern.city_name_check
    city_name_length = RegexPattern.city_name_length_check
    email_format = RegexPattern.email_format_check
    email_domain_extension = RegexPattern.email_domain_extension_check
    email_allowed_chars = RegexPattern.email_allowed_chars_check



class Validator:
    """
    создаем класс validator для следования принципам работы SOLID и так же скрытия сложной структуры
    так же используем статический метод @staticmethod,
    что бы не создавать в будущем отдльные объекты Valodator() это класса
    """

    @staticmethod
    def is_valid(string: str, validation_type: ValidationType) -> bool:
        return bool(re.fullmatch(validation_type.value, string))


# Проверяем телефонный номер
is_phone_ok = Validator.is_valid("123456789", ValidationType.phone_number)
print(is_phone_ok)  # True
