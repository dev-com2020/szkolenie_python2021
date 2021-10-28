from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print("Tu", self.gatunek, ".Startuje i zaraz osiągnę prędkość", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def __init__(self,szybkosc):
        super().__init__("Orzeł",szybkosc)

    def poluj(self):
        print("Tu", self.gatunek, ".Rozpocząłem polowanie!")

    def wydajOdglos(self):
        print("weerrrrd")


class Pingwin(Ptak):

    def __init__(self):
        super().__init__("Pingwin",0)

    def slizgaj(self):
        print("Tu", self.gatunek, ".Rozpocząłem śliźganie!")

    def lec(self):
        print("Tu", self.gatunek, ".Ja nie umiem latać...")

    def wydajOdglos(self):
        print("kwwwwwiii")
