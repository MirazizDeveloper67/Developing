def mijoz_haqida(ism, familiya, t_yil, t_joyi, email="", tel=None):
    yosh = 2026 - t_yil
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "t_yil": t_yil,
        "yosh": yosh,
        "t_joyi": t_joyi,
        "email": email,
        "tel": tel
    }
    return mijoz

def eng_katta(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def aylana_info(r):
    pi = 3.14159
    info = {
        "radius": r,
        "diametr": 2 * r,
        "perimetr": 2 * pi * r,
        "yuzi": pi * (r ** 2)
    }
    return info

def tub_sonlar(min_son, max_son):
    tublar = []
    for n in range(min_son, max_son + 1):
        if n > 1:
            is_tub = True
            for i in range(2, n):
                if n % i == 0:
                    is_tub = False
                    break
            if is_tub:
                tublar.append(n)
    return tublar

def fibonavchi(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    sonlar = [1, 1]
    while len(sonlar) < n:
        sonlar.append(sonlar[-1] + sonlar[-2])
    return sonlar

print("1-topshiriq:")
print(mijoz_haqida("Ali", "Valiyev", 2000, "Toshkent", tel="991234567"))

print("\n2-topshiriq:")
mijozlar = []
while True:
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    t_yil = int(input("Tug'ilgan yil: "))
    t_joyi = input("Tug'ilgan joy: ")
    
    mijoz = mijoz_haqida(ism, familiya, t_yil, t_joyi)
    mijozlar.append(mijoz)
    
    javob = input("Yana mijoz qo'shasizmi? (ha/yo'q): ")
    if javob.lower() != 'ha':
        break

for m in mijozlar:
    print(m["ism"], m["familiya"], m["yosh"], "yoshda")

print("\n3-topshiriq:")
print(eng_katta(10, 25, 15))

print("\n4-topshiriq:")
print(aylana_info(5))

print("\n5-topshiriq:")
print(tub_sonlar(1, 20))

print("\n6-topshiriq:")
print(fibonavchi(10))
