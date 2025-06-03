def zad1(word):
    d, d2, d3, d4 = {}, {}, {}, {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

        if i.isalpha():
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        if i.isalpha():
            i = i.lower()
            if i in d3:
                d3[i] += 1
            else:
                d3[i] = 1

        if i.isalpha():
            i = i.lower()
            if i in d4:
                d4[i] += 1
            else:
                d4[i] = 1

    d4 = sorted(d4.items(), key=lambda item: item[1], reverse=True)

    print(d4[0])


def main():
    zad1("anAnas2")


if __name__ == "__main__":
    main()
