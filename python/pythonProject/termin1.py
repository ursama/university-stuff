class Segregator:
    def __init__(self, maxKartek=500, ileStron=0):
        self._max = maxKartek
        self._ile = ileStron

    def ileWlozonych(self):
        return self._ile

    def ilePomiesci(self):
        return self._max - self._ile

    @property
    def ile(self):
        return self._ile

    @ile.setter
    def ile(self, value):
        if 0 <= value <= self._max:
            self._ile = value
        else:
            raise ValueError

    @ile.deleter
    def ile(self):
        self._ile = 0

    def oproznij(self):
        self._ile = 0

    def __add__(self, other):
        if isinstance(other, Segregator):
            nowa_ilosc_kartek = self._ile + other._ile
            nowy_max = self._max + other._max
            return Segregator(nowy_max, nowa_ilosc_kartek)
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, Segregator):
            return self._max > other._max
        else:
            raise TypeError

    def __str__(self):
        return f"Max kartek: {self._max}, Aktualni kartek: {self._ile}"
