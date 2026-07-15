shaxslar = [
    {
        "ism": "Abu Abdulloh Muhammad ibn Ismoil",
        "yil": 810,
        "joy": "Buxoro",
        "umr": 60,
        "asarlar": ["Al-jome' as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag'ir"]
    },
    {
        "ism": "Abdulla Qodiriy",
        "yil": 1894,
        "joy": "Toshkent",
        "umr": 44,
        "asarlar": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"]
    },
    {
        "ism": "Erkin Vohidov",
        "yil": 1936,
        "joy": "Farg'ona",
        "umr": 80,
        "asarlar": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]
    },
    {
        "ism": "Alisher Navoiy",
        "yil": 1441,
        "joy": "Xirot",
        "umr": 60,
        "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub"]
    }
]

for shaxs in shaxslar:
    print(f"{shaxs['ism']} {shaxs['yil']}-yilda {shaxs['joy']}da tavallud topgan. {shaxs['umr']} yil umr ko'rgan.")

print()

for shaxs in shaxslar:
    print(f"{shaxs['ism']} ning mashhur asarlari:")
    for asar in shaxs["asarlar"]:
        print(asar)
    print()



davlatlar = {
    "o'zbekiston": {
        "poytaxt": "Toshkent",
        "hudud": 448978,
        "aholi": 33000000,
        "pul": "so'm"
    },
    "rossiya": {
        "poytaxt": "Moskva",
        "hudud": 17098246,
        "aholi": 144000000,
        "pul": "rubl"
    },
    "aqsh": {
        "poytaxt": "Vashington",
        "hudud": 9631418,
        "aholi": 327000000,
        "pul": "dollar"
    },
    "malayziya": {
        "poytaxt": "Kuala-Lumpur",
        "hudud": 329750,
        "aholi": 25000000,
        "pul": "ringgit"
    }
}


for nom, info in davlatlar.items():
    print(f"{nom.title()}ning poytaxti {info['poytaxt']}")
    print(f"Hududi: {info['hudud']} kv.km")
    print(f"Aholisi: {info['aholi']}")
    print(f"Pul birligi: {info['pul']}")
    print()


davlat = input("Davlat nomini kiriting: ").lower()

if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxt']}")
    print(f"Hududi: {info['hudud']} kv.km")
    print(f"Aholisi: {info['aholi']}")
    print(f"Pul birligi: {info['pul']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
