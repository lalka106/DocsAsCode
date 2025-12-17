# Справочник API

## Класс Calculator

Основной класс для математических операций.

### `add(a, b)`

Складывает два числа.

**Параметры:**

- `a` (float) - первое число
- `b` (float) - второе число

**Возвращает:**

- `float` - сумма a и b

**Пример:**

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)  # Возвращает 8.0
```

### `divide(a, b)`

Делит два числа.

**Параметры:**

- `a` (float) - делимое
- `b` (float) - делитель

**Возвращает:**

- `float` - результат деления

**Исключение:**

- `ValueError` - если `b` равен 0

**Пример:**

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.divide(10, 2)  # Возвращает 5.0

# Вызовет исключение:
# result = calc.divide(5, 0)  # ValueError
```
