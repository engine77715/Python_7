number = 3847
print(number // 10)
print(number % 10)

firs_number = number % 10
number = number // 10
second_number = number % 10
print(second_number, firs_number)
input_list = [1, 2, 3, 4, 5, 6]

result = [input_list[:len(input_list)//2 + len(input_list) % 2], input_list[len(input_list)//2 + len(input_list) % 2:]]

print(result)