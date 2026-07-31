class Shaxs:
    def __init__(self, ism, familiya, pasport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil

    def get_info(self):
        return f"{self.ism} {self.familiya}, Pasport: {self.pasport}, T-yil: {self.tyil}"


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def get_info(self):
        return f"Fan: {self.nomi}"


class Talaba(Shaxs):
    def __init__(self, ism, familiya, pasport, tyil, idraqam):
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []

    def get_info(self):
        return f"{self.ism} {self.familiya}, ID: {self.idraqam}, {self.bosqich}-bosqich talabasi"

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
        return f"{fan.nomi} faniga yozildingiz."

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            return f"{fan.nomi} fani ro'yxatdan o'chirildi."
        else:
            return "Siz bu fanga yozilmagansiz"

    def get_fanlar(self):
        return [fan.nomi for fan in self.fanlar]


class Professor(Shaxs):
    def __init__(self, ism, familiya, pasport, tyil, ilmiy_daraja):
        super().__init__(ism, familiya, pasport, tyil)
        self.ilmiy_daraja = ilmiy_daraja

    def get_info(self):
        return f"Professor: {self.ism} {self.familiya}, Ilmiy darajasi: {self.ilmiy_daraja}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, pasport, tyil, username):
        super().__init__(ism, familiya, pasport, tyil)
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.username} ({self.ism} {self.familiya})"


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, pasport, tyil, username):
        super().__init__(ism, familiya, pasport, tyil, username)

    def get_info(self):
        return f"Admin: {self.username} ({self.ism} {self.familiya})"

    def ban_user(self):
        print("Foydalanuvchi bloklandi")


# Kodni tekshirib ko'rish:

matematika = Fan("Matematika")
fizika = Fan("Fizika")
tarix = Fan("Tarix")

talaba1 = Talaba("Ali", "Valiyev", "AB1234567", 2002, "000123")

print(talaba1.fanga_yozil(matematika))
print(talaba1.fanga_yozil(fizika))

print("Yozilgan fanlar:", talaba1.get_fanlar())

print(talaba1.remove_fan(fizika))
print(talaba1.remove_fan(tarix))

prof = Professor("Hasan", "Husanov", "AC9876543", 1975, "Doctor")
print(prof.get_info())

admin1 = Admin("Otabek", "Aliyev", "AD5554433", 1995, "admin01")
print(admin1.get_info())
admin1.ban_user()
