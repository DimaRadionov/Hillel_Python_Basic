# Введення речення з двох слів
sentence = input("Введіть речення з двох слів: ")

# Розділення речення на два слова
word1, word2 = sentence.split()

# Форматування змінних трьома різними способами
formatted_str1 = "!%s %s?" %(word2.upper(), word1.capitalize())
formatted_str2 = "!{1} {0}?".format(word1.capitalize(), word2.upper(), '!')
formatted_str3 = f"!{word2.upper()} {word1.capitalize()}?"

source_file = open('test.txt', 'w')

# Вивід результатів
print(sentence, formatted_str1, formatted_str2, formatted_str3, sep='<<<>>>', file=source_file)
