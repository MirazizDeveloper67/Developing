def tugilgan_yil_hisobla(ism, yosh):
    tugilgan_yil = 2026 - yosh
    print(f"{ism.title()}, siz {tugilgan_yil}-yilda tug'ilgansiz.")


def kvadrat_va_kub(son):
    print(f"{son} ning kvadrati: {son**2}")
    print(f"{son} ning kubi: {son**3}")


def juft_yoki_toq(son):
    if son % 2 == 0:
        print(f"{son} — juft son.")
    else:
        print(f"{son} — toq son.")


def kattasini_top(son1, son2):
    if son1 > son2:
        print(f"Kattasi: {son1}")
    elif son2 > son1:
        print(f"Kattasi: {son2}")
    else:
        print("Sonlar teng")


def darajaga_oshir(x, y=2):
    print(f"{x} ning {y}-darajasi: {x**y}")


def bolinish_alomatlari(son):
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi")


tugilgan_yil_hisobla("ali", 25)
kvadrat_va_kub(5)
juft_yoki_toq(7)
juft_yoki_toq(10)
kattasini_top(15, 20)
kattasini_top(8, 8)
darajaga_oshir(5, 3)
darajaga_oshir(4)
bolinish_alomatlari(70)
