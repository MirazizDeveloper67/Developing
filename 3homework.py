davlatlar = {
    "AQSH": "Washington D.C.",
    "ITALIYA": "Rim",
    "MALAYZIYA": "Kuala-Lumpur",
    "O'ZBEKISTON": "Toshkent",
    "QIRG'IZISTON": "Bishkek",
    "QOZOQ'ISTON": "Nursulton",
    "ROSSIYA": "Moskva",
    "SINGAPUR": "Sungapur",
    "TOJIKISTON": "Dushanbe"
}

print("Qaysi davlatning poytaxtini bilishni istaysiz?")
davlat = input().strip().upper()

if davlat in davlatlar:
    print(davlat + "ning poytaxti " + davlatlar[davlat])
else:
    print("Kechirasiz, bizda bunday ma'lumot yo'q")


print("\n=== Restoran menyusi ===")

menu = {
    "osh": 20000,
    "non": 4000,
    "manti": 15000,
    "lagmon": 18000,
    "shashlik": 25000,
    "somsa": 8000,
    "choy": 3000,
    "kofe": 12000,
    "salat": 10000,
    "qazi": 35000
}

buyurtma1 = input("1-taom: ").lower()
buyurtma2 = input("2-taom: ").lower()
buyurtma3 = input("3-taom: ").lower()

narx1 = menu.get(buyurtma1, 0)
narx2 = menu.get(buyurtma2, 0)
narx3 = menu.get(buyurtma3, 0)

if narx1 > 0:
    print(buyurtma1 + " " + str(narx1) + " so'm")
else:
    print("Kechirasiz, " + buyurtma1 + " yo'q")

if narx2 > 0:
    print(buyurtma2 + " " + str(narx2) + " so'm")
else:
    print("Kechirasiz, " + buyurtma2 + " yo'q")

if narx3 > 0:
    print(buyurtma3 + " " + str(narx3) + " so'm")
else:
    print("Kechirasiz, " + buyurtma3 + " yo'q")

jami = narx1 + narx2 + narx3
print("Jami: " + str(jami) + " so'm")
