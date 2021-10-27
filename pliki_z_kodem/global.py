def powiel(tekst="Nie podałeś wartości", ile=1):
    print((tekst + " ") * ile)


# powiel(ile=5, tekst="OJ!")

def duzo(*nazwy, **knazwy):
    print(nazwy)
    print(knazwy)


# duzo(8, 6)
global a
a = 5

def mam_global():

    a = 1
    b = 2
    return a+b

def nie_mam_globala():
    c = 3
    return a+c

print(mam_global())
print(nie_mam_globala())
print(a)