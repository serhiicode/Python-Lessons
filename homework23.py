text = input('Введіть текст: \n')
words = []
words = text.replace(",","").replace(".","").lower().split()
dict = {}
maxnum = 0
maxkey = ""

for i in words:
    dict[i] = words.count(i)

for x, y in dict.items():
    if dict[x] >= maxnum:
        maxnum = dict[x]
        maxkey = x

print(f'Найчастіше слово це: {maxkey}, кількість в тексті: {maxnum}')