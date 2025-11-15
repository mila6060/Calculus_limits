from calculator import calculate_limit

def main():
    print("🧮 КАЛЬКУЛЯТОР ПРЕДЕЛОВ")
    print("Для выхода введите 'exit'")
    
    while True:
        print("\n" + "=" * 40)
        function = input("Введите функцию (например: x**2): ")
        
        if function.lower() in ['exit', 'выход']:
            break
            
        variable = input("Введите переменную (например: x): ")
        point = input("Введите точку (например: 2 или inf): ")
        
        try:
            result = calculate_limit(function, variable, point)
            print(f"✅ Результат: {result}")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    
    print("\nПрограмма завершена!")

if __name__ == "__main__":
    main()
