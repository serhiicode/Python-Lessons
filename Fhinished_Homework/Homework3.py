n, k = int(input("Скільки школярів?\n")), int(input("Скільки яблук?\n"))
ostanetsa_v_korzine = k % n
yablok_na_shkolnika = k // n
print(f"Всі школяри отримають по {yablok_na_shkolnika}, а в корзині залишиться {ostanetsa_v_korzine} яблук.")
