def format_time(seconds):
    # Знайти кількість днів, годин, хвилин та секунд
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)

    # Підбір слова "день" в залежності від кількості днів
    day_word = "днів" if days != 1 else "день"

    # Форматування результату з додаванням провідних нулів
    result = "{:02} днів {:02}:{:02}:{:02}".format(int(days), int(hours), int(minutes), int(seconds))
    return result


# Зчитування введеного користувачем числа секунд
while True:
    try:
        user_input = int(input("Введіть кількість секунд (більше або дорівнює 0 і менше ніж 8640000): "))
        if 0 <= user_input < 8640000:
            break
        else:
            print("Будь ласка, введіть число в межах вказаного діапазону.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Форматування та виведення результату
formatted_time = format_time(user_input)
print("Час у читабельному форматі:", formatted_time)