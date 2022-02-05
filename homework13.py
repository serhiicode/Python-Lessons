s = input("Введіть шось\n")

start = s.find("h") + 1
stop = s.rfind("h") - 1

new_s2 = s[0:s.find("h")+1] + s[start:stop].replace("h", "H") + s[s.rfind("h"):len(s)]

print(new_s2)