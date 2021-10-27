# lambda <parametry> : <wyrażenie>
from functools import reduce

lista = [1, 3, 5, 7]

print(f"Nasza lista: {lista}\n")
print(f"Zastosowanie map: {list(map(lambda _: _ * 2, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda _: _ > 3, lista))}")
print(f"Zastosowanie reduce: {reduce(lambda x, y: x + y, lista)}")

