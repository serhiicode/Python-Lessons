from random import randint

lst1 = [randint(1, 9) for _ in range(0, 15)]
lst2 = [randint(1, 9) for _ in range(0, 15)]
lst3 = lst1 + lst2
s = {element for element in lst3}

print(f'Значення в 2х списках:\n{lst3}\n')
print(f'В списку {len(s)} унікальних значень.')