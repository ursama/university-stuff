def zad1():
    with open("hello.txt", "w") as file:
        file.write("Hello, World!")

    with open("hello.txt", "r") as file:
        data = file.read()
        print(data)


def zad2():
    file_name = input("Wprowadz nazwe pliku input: ")
    file_name2 = input("Wprowadz nazwe pliku output: ")
    try:
        with open(file_name, "r") as input_file:
            lines = input_file.readlines()

        with open(file_name2, "w") as output_file:
            line_nr = 1
            for line in lines:
                output_file.write(f"{line_nr}. {line}")
                line_nr += 1
    except FileNotFoundError:
        exit("Podano zla nazwe pliku")


def main():
    zad2()


if __name__ == "__main__":
    main()
