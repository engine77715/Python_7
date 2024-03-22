def popular_words(text, words):
    text_lower = text.lower()
    # Розділяємо текст на окремі слова
    text_words = text_lower.split()
    # Ініціалізуємо словник, в якому ключі будуть слова зі списку, а значення - кількість їх появ у тексті
    word_count = {word: text_words.count(word) for word in words}
    return word_count


# Перевірка
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')