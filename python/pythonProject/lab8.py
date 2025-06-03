def zad2():
    n = int(input("Wprowadz liczbe calkowita: "))
    for i in range(0, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        print(i)


def zad4():
    lim = float(input("Wpisz limit: "))
    nr_sum = 0
    while True:
        x = float(input("Wprowadz liczbe do sumy: "))
        if x < 0:
            continue
        nr_sum += x
        print(nr_sum)
        if nr_sum > lim:
            break


def try1():
    try:
        n = int(input("Wprowadz liczbe calkowita: "))
    except ValueError:
        exit()

    for i in range(0, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        print(i)


def try2():
    try:
        lim = float(input("Wprowadz liczbe rzeczywista: "))
    except ValueError:
        exit()

    nr_sum = 0
    while True:
        try:
            x = float(input("Wprowadz liczbe do sumy: "))
        except ValueError:
            continue

        if x < 0:
            continue
        nr_sum += x
        print(nr_sum)
        if nr_sum > lim:
            break


def zb1():
    set1 = {1, 2, 4, 5}
    set2 = {2, 3, 5, 6}
    set3 = {4, 5, 6, 7}
    seta = set1 ^ set2
    setb = (set1 | set2 | set3) - (set1 & set2) - (set2 & set3) - (set1 & set3)
    setc = ((set1 & set2) | (set2 & set3) | (set1 & set3)) - (set1 & set2 & set3)
    setd = set([i for i in range(1, 26) if i not in set1])
    print(setd)


def zb2(word1, word2):
    word1, word2 = set(word1), set(word2)
    alphabet = set(chr(i) for i in range(65, 91)) | set(chr(i) for i in range(97, 123))
    seta = set(letter for letter in (word1 & word2) if letter.isalpha())
    setb = set(letter for letter in (word1 | word2) if letter.isalpha())
    print(alphabet)


def main():
    zb2("ananas2", "jablko2")


if __name__ == "__main__":
    main()
