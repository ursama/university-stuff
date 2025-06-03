def main():
    f1([1, 2, 3, 4, 5, 6])


def f1(l):
    counter = 0
    for nr in l:
        if nr % 2 == 0:
            counter += 1


if __name__ == "__main__":
    main()
