import random
import time

# wyniki
user = 0
computer = 0

while True:
    x = input("Wpisz wybór:")
    if x == 'x':
        break
    elif x == 'o':
        x = "orzeł"
    elif x == 'r':
        x = "reszka"
    else:
        print("Proszę dokonać prawidłowego wyboru:")
        print("o - orzeł")
        print("r- reszka")
        print("x - koniec gry")
        continue

    y = random.choice(["orzeł", "reszka"])

    for i in range(0, 3):
        print(3 - i)
        time.sleep(1)

    print("Wynik rzutu:", y)

    if x == y:
        user += 1
    else:
        computer += 1

    print("Wyniki gry:")
    print("Użytkownik:",user)
    print("Komputer:",computer)

