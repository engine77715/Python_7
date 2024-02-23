number = int(input('Введите четырехзначное число:'))
num_1 = number // 1000
num_2 = (number % 1000) // 100
num_3 = (number % 100) // 10
num_4 = number % 10

print(num_1)
print(num_2)
print(num_3)
print(num_4)
