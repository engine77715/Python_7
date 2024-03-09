number = int(input("Введіть ціле число: "))

while number >= 9:
    result = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            result *= digit
        number //= 10
    number = result

print("Результат:", number)