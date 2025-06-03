def main():
    zad1()
    zad2(5)
    zad3()
    zad4_for_end("programming")
    zad5_for_start("H1e2l3l4oW?o!r_l+d")
    zad6_for_start("programming", "studying")


def parse_to_nr(nr):
    try:
        return int(nr)
    except ValueError:
        try:
            return float(nr)
        except ValueError:
            return 0


def zad1():
    # wersja z while
    i = 1
    nrsum = 0
    while i <= 10:
        nr = input(f"Podaj liczbę nr {i}: ")
        nr = parse_to_nr(nr)
        if nr > 0 and isinstance(nr, int):
            nrsum += nr
        i += 1

    print(f"Suma liczb dodatnich i całkowitych to {nrsum}")

    # wersja z for
    nrsum = 0
    for i in range(1, 11):
        nr = input(f"Podaj liczbę nr {i}: ")
        nr = parse_to_nr(nr)
        if nr > 0 and isinstance(nr, int):
            nrsum += nr

    print(f"Suma liczb dodatnich i całkowitych to {nrsum}")


def zad2(quan):
    nrsum = 0
    for i in range(1, quan + 1):
        nr = input(f"Podaj liczbę nr {i}: ")
        nr = parse_to_nr(nr)
        if nr > 0 and isinstance(nr, int):
            nrsum += nr

    print(f"Suma liczb dodatnich i całkowitych to {nrsum}")


def zad3():
    # wersja 1, for
    input_chars = input("Podaj 10 dowolnych znaków (bez spacji): ")
    unique_chars = ""

    for char in input_chars:
        if char not in unique_chars:
            unique_chars += char

    print("Łańcuch wynikowy (unikalne znaki):", unique_chars)

    # wersja 1, while
    input_chars = input("Podaj 10 dowolnych znaków (bez spacji): ")
    unique_chars = ""
    i = 0

    while i < len(input_chars):
        if input_chars[i] not in unique_chars:
            unique_chars += input_chars[i]
        i += 1

    print("Łańcuch wynikowy (unikalne znaki):", unique_chars)

    # wersja 2, for
    unique_chars = ""

    while len(unique_chars) < 10:
        input_chars = input("Podaj znaki (możesz wprowadzić kilka naraz): ")
        for char in input_chars:
            if char not in unique_chars:
                unique_chars += char
                if len(unique_chars) == 10:
                    break

    print("Łańcuch wynikowy o długości 10:", unique_chars)

    # wersja 2, while
    unique_chars = ""

    while len(unique_chars) < 10:
        input_chars = input("Podaj znaki (możesz wprowadzić kilka naraz): ")
        i = 0
        while i < len(input_chars) and len(unique_chars) < 10:
            if input_chars[i] not in unique_chars:
                unique_chars += input_chars[i]
            i += 1

    print("Łańcuch wynikowy o długości 10:", unique_chars)


def zad4_for_start(s):
    count = 0
    for char in set(s):
        if s.count(char) == 2:
            count += 1
    print(f"Ilość znaków występujących dokładnie dwa razy: {count}")


def zad4_for_end(s):
    count = 0
    for char in reversed(list(set(s))):
        if s.count(char) == 2:
            count += 1
    print(f"Ilość znaków występujących dokładnie dwa razy: {count}")


def zad4_while_start(s):
    count = 0
    unique_chars = list(set(s))
    i = 0
    while i < len(unique_chars):
        if s.count(unique_chars[i]) == 2:
            count += 1
        i += 1
    print(f"Ilość znaków występujących dokładnie dwa razy: {count}")


def zad4_while_end(s):
    count = 0
    unique_chars = list(set(s))
    i = len(unique_chars) - 1
    while i >= 0:
        if s.count(unique_chars[i]) == 2:
            count += 1
        i -= 1
    print(f"Ilość znaków występujących dokładnie dwa razy: {count}")


def zad5_for_start(s):
    uppercase = ""
    lowercase = ""
    digits = ""
    others = ""

    for char in s:
        if char.isupper():
            uppercase += char
        elif char.islower():
            lowercase += char
        elif char.isdigit():
            digits += char
        else:
            others += char

    print(uppercase + lowercase + digits + others)


def zad5_for_end(s):
    uppercase = ""
    lowercase = ""
    digits = ""
    others = ""

    for char in reversed(s):
        if char.isupper():
            uppercase += char
        elif char.islower():
            lowercase += char
        elif char.isdigit():
            digits += char
        else:
            others += char

    # Odwrócenie porządku grup, by wynik zachował kolejność
    print(uppercase[::-1] + lowercase[::-1] + digits[::-1] + others[::-1])


def zad5_while_start(s):
    uppercase = ""
    lowercase = ""
    digits = ""
    others = ""

    i = 0
    while i < len(s):
        if s[i].isupper():
            uppercase += s[i]
        elif s[i].islower():
            lowercase += s[i]
        elif s[i].isdigit():
            digits += s[i]
        else:
            others += s[i]
        i += 1

        print(uppercase + lowercase + digits + others)


def zad5_while_end(s):
    uppercase = ""
    lowercase = ""
    digits = ""
    others = ""

    i = len(s) - 1
    while i >= 0:
        if s[i].isupper():
            uppercase += s[i]
        elif s[i].islower():
            lowercase += s[i]
        elif s[i].isdigit():
            digits += s[i]
        else:
            others += s[i]
        i -= 1

    print(uppercase[::-1] + lowercase[::-1] + digits[::-1] + others[::-1])


def zad6_for_start(s1, s2):
    common = ""
    for char in s1:
        if char in s2 and char not in common:
            common += char
    print(common)


def zad6_for_end(s1, s2):
    common = ""
    for char in reversed(s1):
        if char in s2 and char not in common:
            common = char + common
    print(common)


def zad6_while_start(s1, s2):
    common = ""
    i = 0
    while i < len(s1):
        if s1[i] in s2 and s1[i] not in common:
            common += s1[i]
        i += 1
    print(common)


def zad6_while_end(s1, s2):
    common = ""
    i = len(s1) - 1
    while i >= 0:
        if s1[i] in s2 and s1[i] not in common:
            common = s1[i] + common
        i -= 1
    print(common)


if __name__ == "__main__":
    main()
