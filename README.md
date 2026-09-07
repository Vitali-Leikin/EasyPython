# Python Learning Repository 🐍

Добро пожаловать в репозиторий для изучения Python! Этот проект создан для системного и качественного обучения языку Python с соблюдением профессиональных стандартов разработки.

---

## 📋 Содержание

- [Правила написания кода](#правила-написания-кода)
- [Работа с Git](#работа-с-git)
- [Структура репозитория](#структура-репозитория)
- [Как начать](#как-начать)
- [Процесс разработки](#процесс-разработки)

---

## 🎯 Правила написания кода

### 1. **Соответствие PEP 8**

Все код должен соответствовать [PEP 8](https://www.python.org/dev/peps/pep-0008/) - официальному стандарту Python.

**Основные требования:**

- **Отступы:** 4 пробела (не табуляция)
- **Длина строки:** максимум 79 символов (для комментариев и docstring)
- **Импорты:** в начале файла, сгруппированы в порядке: стандартная библиотека, сторонние, локальные
- **Пустые строки:** 2 строки между функциями верхнего уровня, 1 строка между методами класса

```python
# ✅ Правильно
import os
import sys
from typing import List

import requests

from .local_module import helper


def main():
    """Описание функции."""
    pass


class MyClass:
    """Описание класса."""

    def method(self):
        """Описание метода."""
        pass
```

### 2. **Именование**

| Элемент | Стиль | Пример |
|---------|-------|--------|
| Функции | `snake_case` | `calculate_sum()`, `get_user_data()` |
| Переменные | `snake_case` | `user_name`, `max_attempts` |
| Классы | `PascalCase` | `UserManager`, `DataParser` |
| Константы | `UPPER_SNAKE_CASE` | `MAX_RETRIES`, `API_KEY` |
| Приватные методы | `_snake_case` | `_internal_logic()` |
| Магические методы | `__dunder__` | `__init__()`, `__str__()` |

### 3. **Документирование (Docstrings)**

Используйте формат Google-style для docstrings:

```python
def fetch_user_data(user_id: int) -> dict:
    """Получает данные пользователя из базы данных.
    
    Args:
        user_id: Уникальный идентификатор пользователя.
    
    Returns:
        Словарь с данными пользователя.
    
    Raises:
        ValueError: Если user_id отрицательный или нулевой.
        DatabaseError: Если произошла ошибка подключения.
    
    Example:
        >>> data = fetch_user_data(123)
        >>> print(data['name'])
        'John'
    """
    if user_id <= 0:
        raise ValueError("user_id должен быть положительным числом")
    
    return database.query(user_id)
```

### 4. **Типизация (Type Hints)**

Обязательно используйте type hints для лучшей читаемости и поддерживаемости:

```python
from typing import List, Optional, Dict, Union

def process_items(items: List[str], limit: Optional[int] = None) -> Dict[str, int]:
    """Обработка списка элементов."""
    result: Dict[str, int] = {}
    count: int = 0
    
    for item in items:
        if limit and count >= limit:
            break
        result[item] = len(item)
        count += 1
    
    return result
```

### 5. **Обработка ошибок**

```python
# ✅ Правильно - специфичные исключения
try:
    result = int(user_input)
except ValueError:
    print("Ошибка: введите целое число")
except TypeError:
    print("Ошибка: неверный тип данных")

# ❌ Неправильно - общее исключение
try:
    result = int(user_input)
except Exception:
    print("Что-то пошло не так")
```

### 6. **Комментарии**

- Комментарии должны объяснять **почему**, а не **что**
- Короткие комментарии начинаются с `#` и одного пробела
- Не дублируйте код в комментариях

```python
# ✅ Правильно
# Используем сет для O(1) поиска вместо листа O(n)
seen = set()

# ❌ Неправильно
# Добавляем элемент в переменную seen
seen = set()
```

---


```

## 2. 🔧 Работа с Git

### 1. **Git Workflow - Git Flow**

```
main (production)
    ↑
    └─── release branches (v1.0.0)
         ↑
dev (staging)
    ↑
    ├─── feature branches (feature/user-auth)
    ├─── bugfix branches (bugfix/login-error)
    └─── hotfix branches (hotfix/critical-bug)
```

### 2. **Ветки и их назначение**

- `main` - боевой код, только stable версии
- `develop` - интеграционная ветка для разработки
- `feature/*` - новая функциональность
- `bugfix/*` - исправление багов в develop
- `hotfix/*` - критичные исправления в production

### 3. **Правила именования веток**

```bash
# Новая функция
git checkout -b feature/user-authentication

# Исправление бага
git checkout -b bugfix/login-validation-error

# Критичное исправление
git checkout -b hotfix/database-connection-crash

# Отформатировано как: type/brief-description
# Всегда на английском, kebab-case
```

### 4. **Правила коммитов**

**Формат сообщения коммита:**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type (тип коммита):**
- `feat` - новая функциональность
- `fix` - исправление бага
- `docs` - документация
- `style` - форматирование, стиль кода (без изменения логики)
- `refactor` - рефакторинг кода
- `perf` - улучшение производительности
- `test` - добавление или изменение тестов
- `chore` - изменения в конфиге, зависимостях

**Примеры коммитов:**

```bash
# ✅ Правильно
git commit -m "feat(auth): add user login functionality"
git commit -m "fix(parser): handle empty XML tags correctly"
git commit -m "docs: update API endpoint documentation"
git commit -m "refactor(core): simplify data validation logic"

# ❌ Неправильно
git commit -m "fixed stuff"
git commit -m "WIP: working on new feature"
git commit -m "asdf"
```

**Правила сообщений:**

1. Первая строка - максимум 50 символов
2. Вторая строка - пустая
3. Остальное - детальное описание, максимум 72 символа в строке
4. На английском языке
5. Используйте императив ("add", "fix", а не "added", "fixed")

### 5. **Создание Pull Request**

**Перед созданием PR:**

```bash
# Обновите ветку
git fetch origin
git rebase origin/develop

# Запустите все проверки локально
make lint
make test

# Убедитесь что все коммиты хорошо сформированы
git log origin/develop..HEAD
```

**Шаблон PR описания:**

```markdown
## Описание
Краткое описание изменений.

## Связанные issues
Closes #123

## Тип изменения
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📚 Documentation
- [ ] ♻️ Refactoring

## Как протестировать
Шаги для проверки функциональности.

## Checklist
- [ ] Код соответствует PEP 8
- [ ] Добавлены/обновлены тесты
- [ ] Обновлена документация
- [ ] Нет конфликтов с develop
- [ ] Все CI checks пройдены
```

---

## 3. 🚀 Как начать

### 1. **Клонирование репозитория**

```bash
git clone <repository-url>
cd repository
```

### 2. **Установка зависимостей**

```bash
# Создание виртуального окружения (Python 3.9+)
python -m venv venv

# Активация виртуального окружения
# Windows
venv\Scripts\activate
# Unix/macOS
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 👥 Процесс разработки

### Для новичков

1. **Выбрать задачу** - найдите issue помеченный `good first issue`
2. **Создать ветку** - `git checkout -b feature/your-feature`
3. **Написать код** - следуйте правилам выше
4. **Написать тесты** - минимум 80% покрытия кода
5. **Создать PR** - заполните шаблон полностью
6. **Получить review** - исправьте замечания

### Для опытных разработчиков

1. Воспринимайте роль ревьюера серьезно
2. Помогайте новичкам в комментариях к PR
3. Предлагайте улучшения, а не критику
4. Убедитесь что код готов к production

---

## 📚 Полезные ресурсы

- [PEP 8 - Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python](https://realpython.com/)
- [Hitchhiker's Guide to Python](https://docs.python-guide.org/)
- [Python Documentation](https://docs.python.org/3/)

---

## 📝 Лицензия

MIT License - см. файл LICENSE

---

## 🤝 Контрибьютинг

Мы приветствуем контрибьюшены! Пожалуйста, следуйте правилам выше и создавайте PR в ветку `develop`.

---

**Последнее обновление:** 2026-09-02  
**Версия:** 1.0.0
