"""
Простой калькулятор пределов функций
"""

import math

def calculate_limit(func, target_point, tolerance=1e-6):
    """
    Вычисляет предел функции в точке
    """
    
    # Пробуем вычислить предел с разных сторон
    left_value = _approach_from_left(func, target_point, tolerance)
    right_value = _approach_from_right(func, target_point, tolerance)
    
    # Если пределы слева и справа равны - возвращаем значение
    if left_value is not None and right_value is not None:
        if abs(left_value - right_value) < tolerance:
            return (left_value + right_value) / 2
    
    return None


def _approach_from_left(func, point, tolerance):
    """Приближаемся к точке слева"""
    values = []
    step = 0.1  # начинаем с шага 0.1
    
    for i in range(10):  # максимум 10 попыток
        x = point - step
        try:
            value = func(x)
            values.append(value)
            
            # Проверяем сходимость
            if len(values) > 1 and abs(values[-1] - values[-2]) < tolerance:
                return values[-1]
                
        except (ZeroDivisionError, ValueError):
            pass
            
        step /= 10  # уменьшаем шаг
    
    return values[-1] if values else None


def _approach_from_right(func, point, tolerance):
    """Приближаемся к точке справа"""
    values = []
    step = 0.1
    
    for i in range(10):
        x = point + step
        try:
            value = func(x)
            values.append(value)
            
            if len(values) > 1 and abs(values[-1] - values[-2]) < tolerance:
                return values[-1]
                
        except (ZeroDivisionError, ValueError):
            pass
            
        step /= 10
    
    return values[-1] if values else None


def check_continuity(func, point):
    """
    Проверяет непрерывность функции в точке
    """
    try:
        # Значение функции в точке
        func_value = func(point)
        
        # Предел в точке
        limit_value = calculate_limit(func, point)
        
        if limit_value is None:
            return False
            
        # Если значение функции равно пределу - функция непрерывна
        return abs(func_value - limit_value) < 1e-6
        
    except:
        return False


def limit_at_infinity(func, large_number=1e10):
    """
    Вычисляет предел функции на бесконечности
    """
    try:
        return func(large_number)
    except:
        return None


# 🎯 ГОТОВЫЕ ФУНКЦИИ ДЛЯ ТЕСТИРОВАНИЯ
def test_function_1(x):
    """f(x) = (x² - 4) / (x - 2)"""
    if x == 2:
        raise ZeroDivisionError
    return (x**2 - 4) / (x - 2)


def test_function_2(x):
    """f(x) = sin(x) / x"""
    if x == 0:
        return 1  # по определению
    return math.sin(x) / x


def test_function_3(x):
    """f(x) = 1 / x"""
    return 1 / x


def test_function_4(x):
    """f(x) = x²"""
    return x**2


def test_function_5(x):
    """f(x) = (x³ - 8) / (x - 2)"""
    if x == 2:
        raise ZeroDivisionError
    return (x**3 - 8) / (x - 2)


def test_function_6(x):
    """f(x) = (√(x+1) - 1) / x"""
    if x == 0:
        raise ZeroDivisionError
    return (math.sqrt(x + 1) - 1) / x