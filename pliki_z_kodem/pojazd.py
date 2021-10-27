class Pojazd:
    """
    jest to klasa opisująca pojazd
    """

    def __init__(self, kolor, marka):
        """ konstruktor """
        self.kolor = kolor
        self.marka = marka

    def hamuj(self):
        print("hamuje....")

    def jedz(self):
        print(f"Auto o kolorze {self.kolor}m i marce {self.marka} jedzie dalej...")


class FordMustang(Pojazd):

    sygnal = "biiiip!"

    def hamuj(self):
        print("Driftuje....a nie hamuje")

