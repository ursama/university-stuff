import datetime


def main():
    # zad15()
    fkwad()


def zad15():
    name = input("Wpisz imie i nazwisko: ")
    age = int(input("Wpisz wiek: "))
    year = datetime.date.today().year
    print(f"{name} urodził/a się w roku {year - age}")


def fkwad():
    a = int(input("Wprowadz a: "))
    b = int(input("Wprowadz b: "))
    c = int(input("Wprowadz c: "))

    d = b**2 - 4 * a * c
    print(d)

    if d >= 0:
        x1 = (0 - b - d ** 0.5) / (2 * a)
        x2 = (0 - b + d ** 0.5) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = (0 - b) / (2 * a)
        
    else:
        print("delta ujemna")


if __name__ == "__main__":
    main()
