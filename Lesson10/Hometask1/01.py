# Заданий рядок у байтовому вигляді
byte_string = b'r\xc3\xa9sum\xc3\xa9'

# Декодування у рядковий вигляд у кодуванні за замовчуванням (utf-8)
decoded_string_utf8 = byte_string.decode('utf-8')
print(f"Декодування в utf-8: {decoded_string_utf8}")

# Перетворення знову на байтовий рядок у кодуванні 'Latin1'
byte_string_latin1 = decoded_string_utf8.encode('latin1')
print(f"Перетворення в 'Latin1': {byte_string_latin1}")

# Декодування у рядок у кодуванні 'Latin1'
decoded_string_latin1 = byte_string_latin1.decode('latin1')
print(f"Декодування в 'Latin1': {decoded_string_latin1}")
