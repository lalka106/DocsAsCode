"""
Простой калькулятор для демонстрации Docs as Code.
"""

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