def strzalka(n=4):
    for j in range(n):
        print(2*" "+n*"0")
    for i in range(n//2+3):
        print(i * " "+(n+4-2*i) * "0")


def rysunek():
    """
    Funkcja która rysuje strzałkę w lewo
    :return: print()
    """
    for i in range(10):
        print(i * "0")
    for i in range(10, 0, -1):
        print(i * "0")

