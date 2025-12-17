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