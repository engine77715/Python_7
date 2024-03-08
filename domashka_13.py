import string

def get_letters_in_range(s):
    start, end = s.split('-')
    letters = string.ascii_letters
    start_index = letters.index(start)
    end_index = letters.index(end)
    return letters[start_index:end_index + 1]

input_str = input("Введіть дві літери через дефіс: ")
result = get_letters_in_range(input_str)
print("Символи між введеними літерами:", result)