storona = int(input("Введіть сторону квадрата:\n"))

def square(num):
  return f"Периметр = {num * 4}\nПлоща = {num * num}\nДіагональ = {round(num * 2 ** 0.5)}"

print(square(storona))