"""
Простой калькулятор для демонстрации Docs as Code.
"""

import math


class Calculator:
    """Класс для базовых арифметических операций."""
    
    def add(self, a: float, b: float) -> float:
        """
        Складывает два числа.
        
        Args:
            a: Первое число
            b: Второе число
            
        Returns:
            Сумма a и b
            
        Example:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
        """
        return float(a + b)
    
    def multiply(self, a: float, b: float) -> float:
        """
        Умножает два числа.
        
        Args:
            a: Первое число
            b: Второе число
            
        Returns:
            Произведение a и b
        """
        return float(a * b)
    

    def divide(self, a: float, b: float) -> float:
        """
        Делит первое число на второе.
        
        Args:
            a: Делимое
            b: Делитель
            
        Returns:
            Результат деления
            
        Raises:
            ValueError: Если делитель равен 0
            
        Example:
            >>> calc = Calculator()
            >>> calc.divide(6, 2)
            3.0
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        """
        Возводит число в степень.
        
        Args:
            base: Основание
            exponent: Показатель степени
            
        Returns:
            base в степени exponent
            
        Example:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
            
            >>> calc.power(4, 0.5)
            2.0  # квадратный корень
        """
        return math.pow(base, exponent)
    
    def sqrt(self, number: float) -> float:
        """
        Вычисляет квадратный корень числа.
        
        Args:
            number: Число для извлечения корня
            
        Returns:
            Квадратный корень из number
            
        Raises:
            ValueError: Если number отрицательный
            
        Example:
            >>> calc = Calculator()
            >>> calc.sqrt(16)
            4.0
            
            >>> calc.sqrt(-1)
            Traceback (most recent call last):
            ...
            ValueError: Нельзя извлечь корень из отрицательного числа
        """
        if number < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа")
        return math.sqrt(number)