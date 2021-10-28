class Czlowiek:

    def __init__(self, imie, wiek, plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print("Cześć mam na imię", self.imie)

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def mysl(self):
        if self.wiek < 2:
            print("Ja dopiero się uczę!")
        else:
            print("Już sobie myślę....")
