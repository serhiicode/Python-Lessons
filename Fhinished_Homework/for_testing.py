d = {}
print(type(d), d)
d = dict()
print(type(d), d)

d = {
  1: 'one', 
  2: 'two'
}

print(type(d), d)

lst = [
  (0, 'zero'),
  (1, 'one'),
  (2, 'two')
]

d = dict(lst)
print(d[1])

person = {}
person['name'] = 'Ivan'
person['surname'] = 'Ivanov'
person['age'] = 35
person['chilren'] = ['petr','olga']
person['pets'] = {'dog': 'sharik', 'cat': 'marsik'}
print(person)