def main():
    # zad2()
    # zad3()
    # zad4()
    # zad5()
    # zad6()
    zad9()


def zad2():
    x = "kaja"
    print(type(x))

    x = 15
    print(type(x))

    x = -3.5
    print(type(x))


def zad3():
    y = "temp"

    while y != "quit":
        y = int(input("Wprowadz dane: "))
        print(type(y))


def zad4():
    text = "Hello world"
    print(text)


def zad5():
    try:
        print(1/0)
    except:
        print("Nie dzielimy przez 0")

    try:
        print(y)
    except:
        print("Zmienna niezdefiniowana")


def zad6():
    a = int(input("Wprowadz 1. liczbe: "))
    b = int(input("Wprowadz 2. liczbe: "))

    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a // b = {a // b}")
    print(f"a % b = {a % b}")
    print(f"a ** b = {a ** b}")


def zad9():
    print("*" * 5, sep='')
    print(" " * 4 + "*", sep='')
    print(" " * 4 + "*", sep='')
    print(" " * 4 + "*", sep='')
    print(" " * 4 + "*", sep='')
    print(" " * 4 + "*", sep='')
    print("*" + " " * 3 + "*", sep='')
    print(" " + "*" * 3 + " ", sep='')


if __name__ == "__main__":
    main()
