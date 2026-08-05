import json


data = {
    "Model": "Malibu",
    "Rang": "Qora",
    "Yil": 2020,
    "Narx": 40000
}

data_json = json.dumps(data, ensure_ascii=False, indent=4)

print("1-topshiriq: 'data' o'zgaruvchisining JSON ko'rinishi:")
print(data_json)
print("-" * 50)


talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

talaba = json.loads(talaba_json)

print("2-topshiriq: talabaning ismi va familiyasi:")
print(f"Ism: {talaba['ism']}")
print(f"Familiya: {talaba['familiya']}")
print("-" * 50)


with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open("talaba.json", "w", encoding="utf-8") as f:
    json.dump(talaba, f, ensure_ascii=False, indent=4)

print("3-topshiriq: 'data.json' va 'talaba.json' fayllari saqlandi.")
print("-" * 50)


with open("students.json", "r", encoding="utf-8") as f:
    students_data = json.load(f)

print("4-topshiriq: talabalar ro'yxati:")
for student in students_data["student"]:
    ism = student["name"]
    familiya = student["lastname"]
    kurs = student["year"]
    fakultet = student["faculty"]
    print(f"{ism} {familiya}, {kurs}-kurs, {fakultet} talabasi")