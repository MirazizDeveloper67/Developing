otam = {
    "ismi": "Mavlutdin",
    "tugilgan_yili": 1954,
    "tugilgan_joyi": "Samarqand viloyati"
}

print("Otamning ismi", otam["ismi"] + ",", otam["tugilgan_yili"], "-yilda,", otam["tugilgan_joyi"], "da tug'ilgan.")

taomlar = {
    "Ali": "osh",
    "Vali": "somsa",
    "Gulnora": "lagmon",
    "Aziz": "shashlik",
    "Laylo": "manti"
}

print("Alining sevimli taomi:", taomlar["Ali"])
print("Gulnoraning sevimli taomi:", taomlar["Gulnora"])
print("Azizning sevimli taomi:", taomlar["Aziz"])

python_lugati = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "if": "Agar shart",
    "else": "Aks holda",
    "print": "Ekran chiqarish",
    "input": "Foydalanuvchidan ma'lumot olish",
    "dict": "Lug'at",
    "list": "Ro'yxat",
    "for": "Tsikl"
}

kalit = input("\nKalit so'z kiriting: ")

if kalit in python_lugati:
    print(python_lugati[kalit])
else:
    print("Bunda so'z mavjud emas")
