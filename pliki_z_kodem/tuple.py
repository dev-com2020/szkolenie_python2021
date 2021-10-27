
def krotka():
    menu = ("hamburger", "hotdog", "pizza")
    print(menu)
    zamowienie = menu[2:]
    print(zamowienie)

    noweMenu = list(menu)
    menu2 = tuple(noweMenu)
