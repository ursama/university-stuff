import random


def main():
    # wypisz(2.5)

    # for i in range(1, 11):
    #     ile_cyfr(random.randrange(1, 50001))

    # for i in range(1, 11):
    #     nr = int(input("Wprowadź dowolną liczbę całkowitą: "))
    #     odwrotnosc(nr)

    # evensum = 0
    # for i in range(1, 101):
    #     if parzysta(random.randrange(1, 101)):
    #         evensum += 1
    #
    # print(f"Liczby parzyste: {evensum}")

    # i = int(input("Podaj początek przedziału: "))
    # j = int(input("Podaj koniec przedziału: "))
    # if i < j:
    #     k = int(input("Podaj dzielnik: "))
    #     print(f"Liczba wielokrotności liczby {k}: {F(i, j, k)}")
    # else:
    #     print("NIEPOPRAWNE DANE")

    for i in range(1, 11):
        a = int(input("Wpisz a: "))
        n = int(input("Wpisz n: "))
        if a <= 0 or n <= 0:
            print("NIEPOPRAWNE DANE")
        else:
            print(f"Wynik końcowy: {zad06(a, n)}")


def wypisz(arg):
    print(f"Argument tej funkcji: {arg}")


def ile_cyfr(number):
    number = str(number)
    print(f"Ilość cyfr: {len(number)}")


def odwrotnosc(nr):
    print(f"Odwrotność liczby {nr}: {1 / nr}")


def parzysta(nr):
    return nr % 2 == 0


def F(a, b, c):
    div_by_c = 0
    for i in range(a, b + 1):
        if i % c == 0:
            div_by_c += 1

    return div_by_c


def zad06(a, n):
    result = a / (a + 1)
    for i in range(1, n + 1):
        result -= (a + i) / (a + 2**i)

    return result


if __name__ == "__main__":
    main()
