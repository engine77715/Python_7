def common_elements():
    # Генеруємо список чисел, кратних 3
    multiples_of_3 = [i for i in range(1, 101) if i % 3 == 0]

    # Генеруємо список чисел, кратних 5
    multiples_of_5 = [i for i in range(1, 101) if i % 5 == 0]

    # Створюємо множину з перетину двох списків
    common_set = set(multiples_of_3) & set(multiples_of_5)

    return common_set


result = common_elements()
print(result)