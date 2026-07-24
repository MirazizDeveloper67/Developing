import math

print("=== 1-BO'LIM: MATH KUTUBXONASI TOPSHIRIQLARI ===")

x = float(input("1. Haqiqiy son kiriting: "))
print("Natija (math.ceil):", math.ceil(x))
print()

y = float(input("2. Haqiqiy son kiriting: "))
print("Natija (math.floor):", math.floor(y))
print()

print("3. Ikki nuqta koordinatalarini kiriting:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
masofa = math.dist((x1, y1), (x2, y2))
print("Nuqtalar orasidagi masofa:", masofa)
print()

n = float(input("4. Musbat son kiriting (n > 0): "))
log_natija = math.log10(n)
print("O'nlik logarifm (3 xonagacha yaxlitlangan):", round(log_natija, 3))
print()

print("=== 2-BO'LIM: LAMBDA FUNKSIYALARI TOPSHIRIQLARI ===")

kub = lambda a: a ** 3
num = float(input("1. Son kiriting: "))
print("Sonning kubi:", kub(num))
print()

yigindi = lambda a, b: a + b
a = float(input("2. Birinchi sonni kiriting: "))
b = float(input("2. Ikkinchi sonni kiriting: "))
print("Sonlar yig'indisi:", yigindi(a, b))
print()

sonlar_royxati = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toq_sonlar = list(filter(lambda x: x % 2 != 0, sonlar_royxati))
print("3. Asl ro'yxat:", sonlar_royxati)
print("   Ajaratilgan toq sonlar:", toq_sonlar)
print()

kvadratlar = list(map(lambda x: x ** 2, sonlar_royxati))
print("4. Asl ro'yxat:", sonlar_royxati)
print("   Kvadratga oshirilgan ro'yxat:", kvadratlar)
