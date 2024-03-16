def is_palindrome(text):
    # Видалення знаків пунктуації та перетворення на нижній регістр
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Перевірка, чи є очищений текст паліндромом
    return cleaned_text == cleaned_text[::-1]

# Перевірка
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")