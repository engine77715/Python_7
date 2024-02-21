num1 = float(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль"
else:
    result = "Ошибка: неверный оператор"

print("Результат:", result)