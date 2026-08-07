import datetime
import re

print("--- 1. 2 hafta farq bilan 10 ta sana ---")
today = datetime.date.today()

for i in range(10):
    print(today)
    today += datetime.timedelta(weeks=2)


print("\n--- 2. bayramlargacha qolgan kunlar ---")
now = datetime.date.today()

ramazon = datetime.date(2027, 3, 9)
qurbon = datetime.date(2027, 5, 16)

days_ramazon = (ramazon - now).days
days_qurbon = (qurbon - now).days

print("ramazongacha qolgan kunlar:", days_ramazon)
print("qurbon hayitigacha qolgan kunlar:", days_qurbon)


print("\n--- 3. tug'ilgan kundan beri o'tgan vaqt ---")
def get_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    
    years = today.year - birth_year
    months = today.month - birth_month
    days = today.day - birth_day
    
    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12
        
    return f"{years} yil, {months} oy, {days} kun"

print("o'tdi:", get_age(2005, 5, 15))


print("\n--- 4. telefon raqamini tekshirish ---")
phone = input("telefon raqamingizni kiriting (+998XXXXXXXXX): ")

if re.match(r"^\+998\d{9}$", phone):
    print("raqam to'g'ri!")
else:
    print("xato format!")


print("\n--- 5. matndan havolani ajratib olish ---")
def find_urls(text):
    return re.findall(r"https?://[^\s]+", text)

sample_text = "mening saytim https://google.com yoki http://yandex.ru ga kiring"
links = find_urls(sample_text)

print("topilgan havolalar:", links)
