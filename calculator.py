import sympy as sp
from sympy import symbols, limit, oo

def calculate_limit(expression, variable, point):
    """
    Вычисляет предел функции в точке
    """
    try:
        # Создаем символьную переменную
        var = symbols(variable)
        
        # Обрабатываем бесконечность
        if point.lower() in ['inf', '∞']:
            point_val = oo
        elif point.lower() in ['-inf', '-∞']:
            point_val = -oo
        else:
            # Преобразуем в число
            point_val = float(point)
        
        # Преобразуем строку в математическое выражение
        expr = sp.sympify(expression)
        
        # Вычисляем предел
        result = limit(expr, var, point_val)
        
        return result
        
    except ValueError:
        raise Exception("Неправильный формат числа")
    except sp.SympifyError:
        raise Exception("Неправильное математическое выражение")
    except Exception as e:
        raise Exception(f"Ошибка вычисления: {e}")
