# Запитуємо в користувача кількість секунд
total_seconds = int(input("Введіть кількість секунд: "))

# Розраховуємо кількість днів, годин, хвилин і секунд
days = total_seconds // (24 * 3600)
hours = (total_seconds % (24 * 3600)) // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Форматуємо вивід у відповідному форматі
result = f"{days} {'день' if days == 1 else 'дні' if days > 1 else ''}, "
result += f"{hours:02}:{minutes:02}:{seconds:02}"

# Виводимо результат
print(result)