import random

class Adres:
    def __init__(self, nr_domu, ulica, miasto, kod, nr_mieszkania=None):
        self.nr_domu = nr_domu
        self.ulica = ulica
        self.miasto = miasto
        self.kod = kod
        if nr_mieszkania:
            self.nr_mieszkania = nr_mieszkania

    def pokaz(self):
        print(f"Ulica: {self.ulica} \n{self.kod}, {self.miasto}")

    def przed(self, other):
        if isinstance(other, Adres):
            return self.kod < other.kod
        return "Drugi element nie jest obiektem klasy Adres"


class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynik_cal = 0
        self.quiz_liczba = 0

    def getName(self):
        return self.imie

    def addQuiz(self, score):
        self.wynik_cal += score
        self.quiz_liczba += 1

    def getTotalScore(self):
        return f"Laczny wynik: {self.wynik_cal}"

    def getAverageScore(self):
        avg = self.wynik_cal / self.quiz_liczba
        return avg


class Kot:
    def __init__(self, imie="Filemon"):
        self.imie = imie
        self.ulubione = ["mysz"]
        self.nielubiane = ["pies"]
        self.zauwazone = []

    def przywitanie(self):
        print(f"Cześć, mam na imię {self.imie}")

    def pokaz_ulubione(self):
        print(f"Mam {len(self.ulubione)} ulubione zabawki, są to: ")
        for zabawka in self.ulubione:
            print(zabawka)

    def pokaz_nielubiane(self):
        print(f"Mam {len(self.nielubiane)} rzeczy, których nie lubię. Są to:")
        for zabawka in self.nielubiane:
            print(zabawka)

    def polub_nowa_zabawke(self, zabawka):
        if zabawka not in self.ulubione:
            if zabawka in self.nielubiane:
                self.polub_nielubiana_zabawke()
            else:
                self.ulubione.append(zabawka)
                print(f"Polubiłem zabawkę {zabawka}")
        else:
            print(f"Już wcześniej lubiłem {zabawka}")

    def odlub_zabawke(self, zabawka):
        if zabawka in self.ulubione:
            self.ulubione.remove(zabawka)
            self.nielubiane.append(zabawka)
            print(f"Już nie lubię zabawki {zabawka}")
        elif zabawka not in self.nielubiane:
            self.zauwaz(zabawka)
            print(f"Jeszcze nie wiem co sądzić o {zabawka}")
        else:
            print(f"Już wcześniej nie lubiłem {zabawka}")

    def polub_nielubiana_zabawke(self, zabawka):
        if zabawka in self.nielubiane:
            self.nielubiane.remove(zabawka)
            self.ulubione.append(zabawka)
            print(f"Jednak już lubię {zabawka}")
        else:
            self.polub_nowa_zabawke(zabawka)

    def zauwaz(self, zabawka):
        self.zauwazone.append(zabawka)
        print(f"Zauważyłem {zabawka}")


def main():
    zabawki = ["puste pudelko", "laser", "mysz", "piłka", "poduszka", "koc", "pluszak", "pies"]
    kot = Kot()
    for pudelko in range(10):
        zabawka = zabawki[random.randint(0, len(zabawki) - 1)]
        wybor = random.randint(1, 4)
        if wybor == 1:
            kot.zauwaz(zabawka)
        elif wybor == 2:
            kot.polub_nowa_zabawke(zabawka)
        elif wybor == 3:
            kot.odlub_zabawke(zabawka)

    kot.pokaz_ulubione()
    kot.pokaz_nielubiane()


if __name__ == "__main__":
    main()
