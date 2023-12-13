values = [1, 2, '3', 'forth', 'end', 99, True, None]

result = list(map(lambda x: str(x) if isinstance(x, int) else x, values))

print(result)
