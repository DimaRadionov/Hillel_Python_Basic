inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

filtered_palindromes = filter(lambda x: x.lower() == x.lower()[::-1], inputdata)

result = tuple(filtered_palindromes)

print(result)
