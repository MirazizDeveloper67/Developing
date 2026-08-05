import pickle


bugun_ograngan = """Bugun men quyidagilarni o'rgandim:
- JSON fayllar bilan ishlash (json.dumps, json.loads, json.dump, json.load)
- Matn fayllarni o'qish va yozish (open, read, write)
- pickle moduli yordamida ma'lumotlarni saqlash
- pi sonining raqamlari ichidan qidiruv qilish
"""

with open("bugungi_dars.txt", "w", encoding="utf-8") as f:
    f.write(bugun_ograngan)

with open("bugungi_dars.txt", "r", encoding="utf-8") as f:
    matn = f.read()

print("1-topshiriq: 'bugungi_dars.txt' fayli tarkibi:")
print(matn)
print("-" * 50)


with open("pi_million_digits.txt", "r", encoding="utf-8") as f:
    pi_matn = f.read()

pi_matn = pi_matn.replace("\n", "").replace(" ", "")

print("2-topshiriq: pi_million_digits.txt o'qildi.")
print(f"Fayl uzunligi (belgilar soni): {len(pi_matn)}")
print(f"Boshi: {pi_matn[:20]}...")
print("-" * 50)

pi_kasr_qismi = pi_matn.split(".")[1]


def sana_pi_ichida_bormi(kun, oy, yil, pi_raqamlari):

    sana_str = f"{kun:02d}{oy:02d}{yil:04d}"
    topildi = sana_str in pi_raqamlari

    if topildi:
        joylashuv = pi_raqamlari.index(sana_str)
        return True, joylashuv
    else:
        return False, -1


kun, oy, yil = 25, 2, 2000
natija, orin = sana_pi_ichida_bormi(kun, oy, yil, pi_kasr_qismi)

print("3-topshiriq: sana pi ichida qidirilmoqda...")
print(f"Qidirilayotgan ketma-ketlik: {kun:02d}{oy:02d}{yil:04d}")
if natija:
    print(f"Natija: TOPILDI! {orin}-o'rinda (nuqtadan keyin) joylashgan.")
else:
    print("Natija: TOPILMADI.")
print("-" * 50)


pi_float = float(pi_matn)

with open("pi_float.pkl", "wb") as f:
    pickle.dump(pi_float, f)

print("4-topshiriq: pi float ko'rinishida 'pi_float.pkl' fayliga saqlandi.")
print(f"Saqlangan qiymat (dastlabki bir nechta raqami): {pi_float}")

with open("pi_float.pkl", "rb") as f:
    tekshirish = pickle.load(f)
print(f"Faylni qayta o'qish natijasi float turimi? {type(tekshirish) is float}")
print("-" * 50)


def malumot_yozish(fayl_nomi="malumotlar.txt"):
   
    print("Ma'lumot kiriting (chiqish uchun bo'sh qator kiriting):")
    with open(fayl_nomi, "a", encoding="utf-8") as f:
        while True:
            malumot = input("> ")
            if malumot == "" or malumot.lower() == "chiqish":
                break
            f.write(malumot + "\n")
    print(f"Ma'lumotlar '{fayl_nomi}' fayliga qo'shildi.")


if name == "main":
    print("5-topshiriq: foydalanuvchidan ma'lumot olish dasturi.")
    print("(Bu qismni ishga tushirish uchun quyidagi funksiyani chaqiring)")
    print("malumot_yozish()")