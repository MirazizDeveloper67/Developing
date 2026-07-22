def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija = natija * son
    return natija

def talaba_info(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

print(kopaytma(2, 3, 4))
print(talaba_info("Ali", "Valiyev", yosh=20, kurs=3))
