# 1-topshiriq: Email tekshirish
pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]

for pochta in pochtalar:
    if "@" in pochta:
        print(pochta, "- email tog'ri")
    else:
        print("Noto'g'ri email:", pochta)


# 2-topshiriq: Parol kuchini tekshirish
parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]

for parol in parollar:
    if len(parol) < 8:
        print(parol, "- Juda qisqa")
    elif parol.isalpha():
        print(parol, "- Kuchsiz parol")
    else:
        print(parol, "- Kuchli parol")


# 3-topshiriq: Ob-havo tahlili
haroratlar = [20, 22, 19, 24, 25, 23, 21]
jami = 0

for harorat in haroratlar:
    jami = jami + harorat
    if harorat > 22:
        print(harorat, "- Iliq kun")
    else:
        print(harorat, "- Salqin kun")

ortacha = jami / len(haroratlar)
print("Ortacha harorat:", ortacha)


# 4-topshiriq: Restoran buyurtmalari
taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]

buyurtma = input("Taom kiriting: ")

for taom in taomlar:
    if buyurtma == taom:
        print("Buyurtmangiz qabul qilindi")
        break
else:
    print("Kechirasiz, bunaqa taom yo'q")


# 5-topshiriq: Anketa tahlili
yoshlar = [16, 21, 17, 30, 25]

for yosh in yoshlar:
    if yosh < 18:
        print(yosh, "- Yosh chegarasiga yetmagan")
    else:
        print(yosh, "- Xush kelibsiz")


# 6-topshiriq: Bildirishnomalar
xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]

for xabar in xabarlar:
    if xabar == "Batareya past":
        print("Telefoningizni quvvatlang")


# 7-topshiriq: Fayllarni guruhlash
fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar = []
rasmlar = []

for fayl in fayllar:
    if fayl.find(".jpg") != -1:
        rasmlar.append(fayl)
    elif fayl.find(".mp3") != -1:
        musiqalar.append(fayl)

print("Rasmlar:", rasmlar)
print("Musiqalar:", musiqalar)