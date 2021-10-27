lista = []
lista2 = [1, 2, 3]
lista3 = ["Tomek", 5, 9.78, False]

lista2.reverse()
lista2.append(4)

print(lista)
print(lista2)
print(lista3)
lista3[4:] = [9]
lista3.insert(0, 50)
print(lista3)

print(type(lista))

dni_tyg = ['poniedziałek', 'wtorek', 'środa',
           'czwartek', 'piątek', 'sobota', 'niedziela']


for i in range(len(dni_tyg)):
    print(dni_tyg[i][0].upper(), sep="")


#dni_tyg.pop(0)
# dni_tyg.clear()
# print(dni_tyg)


