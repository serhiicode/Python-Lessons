s = input("Введіть шось\n")

start = s.find("h") + 1
stop = s.rfind("h") 

new_s2 = s[0:start] + s[start:stop].replace("h", "H") + s[stop:len(s)]

print(new_s2)