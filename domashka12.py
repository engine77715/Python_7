# Запитуємо користувача про введення рядка
user_input = input("Введіть рядок: ")

# Розбиваємо рядок на слова, кожне слово капіталізуємо та об'єднуємо їх з # в початку
hashtag = '#' + ''.join(word.capitalize() for word in user_input.split() if word.isalnum())

# Обмежуємо довжину хештегу до 140 символів
hashtag = hashtag[:140]

# Виводимо результат
print("Хештег:", hashtag)