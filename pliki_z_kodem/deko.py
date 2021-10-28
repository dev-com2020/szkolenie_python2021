# def wykonaj(funkcja, a, b):
#     x = funkcja(a, b)
#     return x
#
# def dodaj(a, b):
#     return a + b
#
# def glowna():
#     def wewn(a, b):
#         return a * b
#
#     x = wewn(2, 4)
#     return x
#
# def funk():
#     def funkW(a, b):
#         return a * b
#
#     return funkW
import time


def dekor(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "Wykonywała się", koniec - start, "sekund.")
        return x

    return wew


@dekor
def dodaj(a, b):
    time.sleep(1)
    return a + b


@dekor
def odejmij(a, b, c):
    time.sleep(1)
    return a - b - c


print(dodaj(2, 2))
print(odejmij(1, 2, 3))
