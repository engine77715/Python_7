nums = [0, 1, 0, 12, 3, 0, 8, 33, 22, 0, 0, 15, 11, 18]

# Визначаємо кількість нулів у списку
count_zeros = nums.count(0)

# Видаляємо всі нулі зі списку
nums = [num for num in nums if num != 0]

# Додаємо необхідну кількість нулів в кінець списку
nums += [0] * count_zeros

print(nums)