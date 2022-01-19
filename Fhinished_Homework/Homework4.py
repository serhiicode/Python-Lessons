txt = "Скільки учнів в классі"
k1, k2, k3 = int(input(f"{txt}, №1\n")), int(input(f"{txt}, №2\n")), int(input(f"{txt}, №3\n"))
part1 = k1 // 2 + k1 % 2
part2 = k2 // 2 + k2 % 2
part3 = k3 // 2 + k3 % 2
vsego_part = part1 + part2 + part3
print(f'Потрібно купити {vsego_part} парт(и)!')