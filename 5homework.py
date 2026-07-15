while True:
    rang = input("Svetofor qaysi rangda? ")
    if rang == "qizil" or rang == "sariq" or rang == "yashil":
        print("Rahmat, to'g'ri keladi")
        break
    else:
        print("Xato rang, qayta kiriting")


import random

tasodifiy_son = random.randint(1, 10)

while True:
    urinish = int(input("1 dan 10 gacha son kiriting: "))
    if urinish == tasodifiy_son:
        print("Tabriklaymiz, siz topdingiz!")
        break
    else:
        print("Noto'g'ri, qayta urinib ko'ring")


dostlar = []

while True:
    ism = input("Do'stingizning ismini kiriting (tugatish uchun 'stop'): ")
    if ism == "stop":
        break
    dostlar.append(ism)

print("Sizning do'stlaringiz:")
print(dostlar)


kurs = 12600

while True:
    kiritma = input("Necha so'm almashtirmoqchisiz? (chiqish uchun 'exit'): ")
    if kiritma == "exit":
        print("Dastur to'xtatildi")
        break
    som = float(kiritma)
    dollar = som / kurs
    print(f"{som} so'm = {dollar:.2f} dollar")
