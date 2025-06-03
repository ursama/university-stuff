from laboratorium import *
import random

lista = [random.randint(1, 100) for x in range(10)]


def main():
    # zad1()
    # zad2()
    # lab71(10)
    lab72()


def zad1():
    quantity = [0] * 10
    L = [123, 5, 80, -42, 0]
    L = [str(x * -1) if x < 0 else str(x) for x in L]
    counter = 0
    for char in quantity:
        for nr in L:
            for position in nr:
                if position == str(counter):
                    quantity[counter] += 1
        counter += 1

    print(quantity)


def zad2():
    samogloski = "aeiosuy"
    counter = 0
    letters = [chr(random.randint(97, 122)) for x in range(10)]
    for letter in letters:
        if letter in samogloski:
            counter += 1


def lab71(n):
    numbers = [x for x in range(n) if x % 3 == 0 or x % 5 == 0]
    print(numbers)


def lab72():
    lista = [round(random.uniform(-100, 100), 2) for x in range(random.randint(1, 50))]
    print(lista)


if __name__ == "__main__":
    main()
