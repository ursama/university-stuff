class Czas:
    def __init__(self, przekazana_godzina, przekazana_minuta):
        self.godzina = przekazana_godzina
        self.minuta = przekazana_minuta

    def __add__(self, other):
        if isinstance(other, Czas):
            suma_minut = 0
            suma_minut += (self.godzina * 60) + self.minuta
            suma_minut += (other.godzina * 60) + other.minuta
            self.godzina = suma_minut // 60 % 24
            self.minuta = suma_minut % 60
            print(self)
        else:
            return "Błędne"

    def __sub__(self, other):
        suma_minut = 0
        suma_minut += (self.godzina * 60) + self.minuta
        suma_minut -= (other.godzina * 60) + other.minuta
        suma_minut = abs(suma_minut)
        self.godzina = suma_minut // 60 % 24
        self.minuta = suma_minut % 60
        print(self)

    def __str__(self):
        return f"{str(self.godzina).zfill(2)}:{str(self.minuta).zfill(2)}"


def main():
    godzina_1 = Czas(20, 4)
    godzina_2 = Czas(10, 3)
    godzina_3 = Czas(15, 30)
    godzina_1 + godzina_2
    # godzina_2 - godzina_3


if __name__ == "__main__":
    main()
