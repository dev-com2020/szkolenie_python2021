class Samochod:

    def __init__(self):
        self.__silnik = False
        self.__bieg = 0
        self.__predkosc = 0

    def uruchom(self):
        self.__silnik = True

    def wylacz(self):
        self.__silnik = False

    def __biegWyzej(self):
        if self.__bieg < 6: self.__bieg += 1; print(self.__bieg)  # skrócony zapis!

    def __biegNizej(self):
        if self.__bieg >= 0: self.__bieg -= 1; print(self.__bieg)  # skrócony zapis!

    def przyspiesz(self):
        if self.__silnik == True:
            self.__predkosc += 10
            print(self.__predkosc)
            self.__biegWyzej()

    def hamuj(self):
        if self.__predkosc >= 10:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0
        print(self.__predkosc)
        self.__biegNizej()



