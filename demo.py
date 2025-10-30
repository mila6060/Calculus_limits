"""
Демонстрация работы калькулятора пределов
Показывает все возможности проекта limits_calculator
"""

from limits import calculate_limit, check_continuity, limit_at_infinity
import math


def main():
    print("🎯 ДЕМОНСТРАЦИЯ CALCULUS LIMITS CALCULATOR")
    print("=" * 55)
    
    demonstrate_basic_limits()
    demonstrate_continuity()
    demonstrate_infinity_limits()
    demonstrate_custom_functions()
    demonstrate_error_cases()


def demonstrate_basic_limits():
    """Демонстрация базовых пределов"""
    print("\n📊 1. БАЗОВЫЕ ПРЕДЕЛЫ")
    print("-" * 30)
    
    # Пример 1: Алгебраическая функция
    print("1. Алгебраическая функция:")
    def rational_func(x):
        return (x**2 - 4) / (x - 2) if x != 2 else None
    
    result = calculate_limit(rational_func, 2)
    print(f"   f(x) = (x² - 4) / (x - 2)")
    print(f"   lim при x→2 = {result}")
    print(f"   ✅ Ожидается: 4.0")
    print()
    
    # Пример 2: Тригонометрическая функция
    print("2. Тригонометрическая функция:")
    def trig_func(x):
        return math.sin(x) / x if x != 0 else 1
    
    result = calculate_limit(trig_func, 0)
    print(f"   f(x) = sin(x) / x")
    print(f"   lim при x→0 = {result}")
    print(f"   ✅ Ожидается: 1.0")
    print()
    
    # Пример 3: Функция с корнем
    print("3. Функция с корнем:")
    def sqrt_func(x):
        return (math.sqrt(x + 1) - 1) / x if x != 0 else 0.5
    
    result = calculate_limit(sqrt_func, 0)
    print(f"   f(x) = (√(x+1) - 1) / x")
    print(f"   lim при x→0 = {result}")
    print(f"   ✅ Ожидается: 0.5")
    print()


def demonstrate_continuity():
    """Демонстрация проверки непрерывности"""
    print("\n📈 2. ПРОВЕРКА НЕПРЕРЫВНОСТИ")
    print("-" * 35)
    
    # Пример 1: Непрерывная функция
    print("1. Непрерывная функция:")
    def continuous_func(x):
        return x**2 + 3*x + 1
    
    result = check_continuity(continuous_func, 1)
    print(f"   f(x) = x² + 3x + 1")
    print(f"   Непрерывна в x=1: {result}")
    print(f"   ✅ Ожидается: True")
    print()
    
    # Пример 2: Разрывная функция
    print("2. Разрывная функция:")
    def discontinuous_func(x):
        return 1 / (x - 2) if x != 2 else None
    
    result = check_continuity(discontinuous_func, 2)
    print(f"   f(x) = 1 / (x - 2)")
    print(f"   Непрерывна в x=2: {result}")
    print(f"   ✅ Ожидается: False")
    print()
    
    # Пример 3: Функция с устранимым разрывом
    print("3. Функция с 'дыркой':")
    def hole_func(x):
        return (x**2 - 9) / (x - 3) if x != 3 else 6
    
    result = check_continuity(hole_func, 3)
    print(f"   f(x) = (x² - 9) / (x - 3)")
    print(f"   Непрерывна в x=3: {result}")
    print(f"   ✅ Ожидается: True (разрыв устранен)")
    print()


def demonstrate_infinity_limits():
    """Демонстрация пределов на бесконечности"""
    print("\n∞ 3. ПРЕДЕЛЫ НА БЕСКОНЕЧНОСТИ")
    print("-" * 35)
    
    # Пример 1: Предел на +∞
    print("1. Предел на +∞:")
    def rational_inf(x):
        return (2*x + 1) / x
    
    result = limit_at_infinity(rational_inf)
    print(f"   f(x) = (2x + 1) / x")
    print(f"   lim при x→+∞ = {result}")
    print(f"   ✅ Ожидается: 2.0")
    print()
    
    # Пример 2: Предел на -∞
    print("2. Предел на -∞:")
    result = limit_at_infinity(rational_inf, -1e10)
    print(f"   f(x) = (2x + 1) / x")
    print(f"   lim при x→-∞ = {result}")
    print(f"   ✅ Ожидается: 2.0")
    print()
    
    # Пример 3: Предел обратной функции
    print("3. Обратная функция:")
    def inverse_func(x):
        return 1 / x
    
    result = limit_at_infinity(inverse_func)
    print(f"   f(x) = 1 / x")
    print(f"   lim при x→+∞ = {result}")
    print(f"   ✅ Ожидается: 0.0")
    print()


def demonstrate_custom_functions():
    """Демонстрация пользовательских функций"""
    print("\n🔧 4. ПОЛЬЗОВАТЕЛЬСКИЕ ФУНКЦИИ")
    print("-" * 35)
    
    print("Создайте свою функцию и проверьте предел!")
    print()
    
    # Пример 1: Полином
    print("1. Полиномиальная функция:")
    def custom_poly(x):
        return x**3 - 2*x**2 + x - 5
    
    result = calculate_limit(custom_poly, 2)
    print(f"   f(x) = x³ - 2x² + x - 5")
    print(f"   lim при x→2 = {result}")
    print(f"   Проверка: f(2) = {custom_poly(2)}")
    print()
    
    # Пример 2: Сложная функция
    print("2. Сложная функция:")
    def complex_func(x):
        return (math.sin(2*x) * math.exp(-x)) / x if x != 0 else 2
    
    result = calculate_limit(complex_func, 0)
    print(f"   f(x) = sin(2x) * e^(-x) / x")
    print(f"   lim при x→0 = {result}")
    print()
    
    # Пример 3: Шаблон для пользователя
    print("3. 🎯 ПОПРОБУЙТЕ САМИ!")
    print("   def ваша_функция(x):")
    print("       return ...  # ваша формула")
    print()
    print("   результат = calculate_limit(ваша_функция, точка)")
    print("   print(f'Предел: {результат}')")
    print()


def demonstrate_error_cases():
    """Демонстрация особых случаев"""
    print("\n⚠️  5. ОСОБЫЕ СЛУЧАИ")
    print("-" * 25)
    
    # Пример 1: Предел не существует
    print("1. Предел не существует:")
    def no_limit_func(x):
        return 1 / x if x != 0 else None
    
    result = calculate_limit(no_limit_func, 0)
    print(f"   f(x) = 1 / x")
    print(f"   lim при x→0 = {result}")
    print(f"   ✅ Ожидается: None")
    print()
    
    # Пример 2: Бесконечный предел
    print("2. Бесконечный предел:")
    def infinite_func(x):
        return 1 / (x**2) if x != 0 else None
    
    result = calculate_limit(infinite_func, 0)
    print(f"   f(x) = 1 / x²")
    print(f"   lim при x→0 = {result}")
    print(f"   ⚠️  Может вернуть очень большое число")
    print()
    
    # Пример 3: Особая точка
    print("3. Функция с особенностью:")
    def special_func(x):
        return math.log(abs(x)) if x != 0 else None
    
    result = calculate_limit(special_func, 0)
    print(f"   f(x) = ln|x|")
    print(f"   lim при x→0 = {result}")
    print(f"   ⚠️  Может вернуть -inf")
    print()


def show_usage_guide():
    """Показывает краткое руководство по использованию"""
    print("\n📖 КРАТКОЕ РУКОВОДСТВО")
    print("=" * 25)
    
    print("""
ИМПОРТ ФУНКЦИЙ:
    from limits import calculate_limit, check_continuity, limit_at_infinity

ВЫЧИСЛЕНИЕ ПРЕДЕЛА:
    def f(x):
        return (x**2 - 1) / (x - 1)
    
    result = calculate_limit(f, 1)
    print(f"Предел: {result}")  # Выведет: 2.0

ПРОВЕРКА НЕПРЕРЫВНОСТИ:
    continuous = check_continuity(f, точка)
    print(f"Непрерывна: {continuous}")

ПРЕДЕЛ НА БЕСКОНЕЧНОСТИ:
    result = limit_at_infinity(lambda x: 1/x)
    print(f"Предел: {result}")  # Выведет: 0.0
    """)


if __name__ == "__main__":
    # Запускаем демонстрацию
    main()
    
    # Показываем руководство
    show_usage_guide()
    
    print("\n" + "🎉 ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА!".center(55))
    print("✨ Проект готов к использованию и защите!".center(55))