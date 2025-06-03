def main():
    # zad01()
    # zad02()
    # zad06(104)
    # zad10()
    zad12()


def zad01():
    for i in range(1, 65):
        print("Hello world")


def zad02():
    nrsum = 0
    for i in range(1, 11):
        nrsum += i
    print(f"Suma: {nrsum}")


def zad06(num):
    copynum = num
    divider = 2
    dividers = []
    while copynum > 1:
        if copynum % divider == 0:
            copynum /= divider
            dividers.append(divider)
        else:
            divider += 1

    print(f"Lista czynników pierwszych liczby {num}: {dividers}")


def zad10():
    tries = 0

    while True:
        password = input("Password: ")

        if password == "1979":
            print("Correct password.")
            break
        elif tries < 4:
            tries += 1
            print(f"Incorrect password. You have {5 - tries} more tries. \n")
        else:
            print("You typed incorrect password too many times.")
            break


def zad12():
    char = input("Type a character: ")
    columns = int(input("Type a number of columns: "))
    quantity = columns + 1

    while quantity > 1:
        quantity -= 1
        print(quantity * char)

    while quantity < columns:
        quantity += 1
        print(quantity * char)


if __name__ == "__main__":
    main()
