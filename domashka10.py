import string
import keyword

# Запитуємо користувача про рядок
user_input = input("Введіть рядок: ")

# Перевіряємо, чи починається рядок з цифри
if user_input[0] in "0123456789":
    print(False)
else:
    # Перевіряємо, чи містить рядок великі літери, пробіл і знаки пунктуації, окрім "_"
    contains_punctuation = False
    contains_upper = False
    for char in user_input:
        if char in string.punctuation and char != "_":
            contains_punctuation = True
            break
        if char.isupper() or char.isspace():
            contains_upper = True
            break

    if contains_punctuation or contains_upper:
        print(False)
    else:
        # Перевіряємо, чи не збігається рядок з зарезервованими ключовими словами
        is_keyword = False
        for word in keyword.kwlist:
            if user_input == word:
                is_keyword = True
                break

        if is_keyword:
            print(False)
        else:
            print(True)