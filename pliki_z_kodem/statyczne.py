class Licznik:
    ile = 0  # pole statyczne

    def __init__(self):
        Licznik.ile += 1  # odwołanie do pola statycznego
        self.ktory = Licznik.ile
        print(f"To jest obiekt nr {Licznik.ile}")

    def __del__(self):  # destruktor
        Licznik.ile -= 1
        print(f"Niszczę obiekt nr {self.ktory}, pozostało jeszcze {Licznik.ile}")

    @staticmethod
    def policz():
        return Licznik.ile


def main():
    a = Licznik()
    b = Licznik()
    c = Licznik()
    print(f"a to obiekt nr {a.ktory}")
    print(f"b to obiekt nr {b.ktory}")
    print(f"c to obiekt nr {c.ktory}")
    print(f"Liczba obiektów to: {Licznik.policz()}")
    a = None
    b = None
    print(f"Liczba obiektów to: {Licznik.policz()}")

if __name__ == "__main__":
    main()
