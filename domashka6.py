input_list = [1, 2, 3, 4, 5, 6]

result = [input_list[:len(input_list)//2 + len(input_list) % 2], input_list[len(input_list)//2 + len(input_list) % 2:]]

print(result)