import copy

a_1 = (3, 'str', 1)
a_1 = list(a_1)
a_2 = (3, 'str', 1)
a_2 = list(a_2)
print(a_1 == a_2)  # True
print(a_1 is a_2)  # False
# print(id(a_1))
# print(id(a_2))

b_1 = 2
b_1 = copy.copy(b_1)
b_2 = 2
b_2 = copy.copy(b_2)
print(b_1 == b_2)  # True
print(b_1 is b_2)  # True
# print(id(b_1))
# print(id(b_2))
