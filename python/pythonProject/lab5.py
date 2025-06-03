def main():
    # f1("Ala ma Kota")
    # f3("wefawef888aewfwae--++")
    # print(f5("kaja", "kaja"))
    # print(f5("kaja", "mróz"))
    print(mirror("napis"))


def f1(napis):
    fixed_word = ""
    for letter in napis:
        if "a" <= letter <= "z":
            fixed_word += letter
    fixed_word = fixed_word[::-1]

    print(fixed_word)


def f3(napis):
    char_count = 0
    for letter in napis:
        if letter < "A" or letter > "z":
            char_count += 1
    print(f"Liczba znaków innych niż litery alfabetu: {char_count}")


def f5(napis1, napis2):
    return napis1 == napis2


def mirror(napis):
    return napis + napis[::-1]


if __name__ == "__main__":
    main()
