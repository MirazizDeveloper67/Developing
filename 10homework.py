class User:
    def __init__(self, ism, familiya, username, email, telefon):
        self.ism = ism
        self.familiya = familiya
        self.username = username
        self.email = email
        self.telefon = telefon

    def get_full_name(self):
        return f"{self.ism} {self.familiya}"

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.get_full_name()}, email: {self.email}"

    def get_contact(self):
        return f"{self.get_full_name()} bilan bog'lanish: email - {self.email}, tel - {self.telefon}"

    def update_email(self, yangi_email):
        self.email = yangi_email
        return f"Email yangilandi: {self.email}"


user1 = User("Alijon", "Valiyev", "alijon1994", "alijon1994@gmail.com", "+998901234567")
user2 = User("Malika", "Akramova", "malika_a", "malika.a@mail.ru", "+998939876543")

print(user1.get_info())
print(user2.get_info())

print("---")

print(user1.get_full_name())
print(user2.get_contact())

print("---")

print(user1.update_email("alijon_yangi@gmail.com"))
print(user1.get_info())
