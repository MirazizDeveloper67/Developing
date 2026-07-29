class Avto:
    def __init__(self, model, rang, korobka, narx, kilometer=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometer = kilometer

    def get_info(self):
        return (f"Model: {self.model}, Rang: {self.rang}, "
                f"Korobka: {self.korobka}, Narx: {self.narx} so'm, "
                f"Kilometer: {self.kilometer} km")

    def update_km(self, yangi_km):
        self.kilometer += yangi_km
        print(f"{self.model} avtomobilining yangi kilometraji: {self.kilometer} km")


class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avtomobillar = []

    def avto_qoshish(self, avto):
        self.avtomobillar.append(avto)
        print(f"{avto.model} avtosalonga qo'shildi!")

    def barcha_avtolar(self):
        print(f"\n--- {self.nomi} avtosaloni ({self.manzili}) ---")
        if len(self.avtomobillar) == 0:
            print("Hozircha avtomobillar yo'q")
        else:
            for avto in self.avtomobillar:
                print(avto.get_info())


avto1 = Avto("Chevrolet Cobalt", "Oq", "Avtomat", 15000, kilometer=5000)
avto2 = Avto("Chevrolet Nexia", "Qora", "Mexanika", 9000)

print(avto1.get_info())
print(avto2.get_info())

avto1.update_km(200)
avto2.update_km(50)

salon = Avtosalon("AutoDream", "Toshkent, Chilonzor")

salon.avto_qoshish(avto1)
salon.avto_qoshish(avto2)

salon.barcha_avtolar()

print("\n--- dir(avto1) natijasi ---")
print(dir(avto1))

print("\n--- avto1.__dict__ natijasi ---")
print(avto1.__dict__)

print("\n--- dir(str) natijasi ---")
print(dir(str))

print("\n--- dir(int) natijasi ---")
print(dir(int))
