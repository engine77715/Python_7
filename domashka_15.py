def format_time(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Вибираємо правильний варіант слова "день"
    if days == 1:
        days_str = 'день'
    elif 1 < days < 5:
        days_str = 'дні'
    else:
        days_str = 'днів'

    return f"{days} {days_str}, {hours:02}:{minutes:02}:{seconds:02}"


# Перевірка введених даних та виведення результату
while True:
    try:
        seconds = int(input("Введіть кількість секунд (більше 0 і менше 8640000): "))
        if 0 <= seconds < 8640000:
            print(format_time(seconds))
            break
        else:
            print("Неправильне введення. Спробуйте ще раз.")
    except ValueError:
        print("Неправильне введення. Введіть ціле число.")