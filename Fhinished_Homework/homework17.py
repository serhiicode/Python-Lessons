from random import randint

lst = [randint(1, 9) for _ in range(0, 15)]
s = {element for element in lst}

print(f'Згенерований список:\n{lst}\n')
print(f'В списку {len(s)} унікальних значень.')