import time

czas = time.localtime()
print("Godzina", czas[3], "Minuta:", czas[4], "Sekunda:", czas[5])

data = time.strftime("%B %d %Y, %H-%M:%S", time.localtime())
print(data)

"""
  %a - skrócony dzień tygodnia
  %A - pełny dzień tygodnia
  %b - skrócona nazwa miesiąca
  %B - pełna nazwa miesiąca
  %d - dzień miesiąca (01 do 31)
  %D* - to samo, co %m/%d/%y
  %e* - dzień miesiąca (1 do 31)
  %H - godzina (format 24-godzinny) (zakes od 00 do 23)
  %I - godzina (format 12-godzinny) (zakres od 01 do 12)
  %m - miesiąc jako liczba (01 do 12)
  %M - minuty jako liczba
  %p - albo "am" albo "pm" zgodnie z aktualnym czasem
  %R* - czas w notacji 24-godzinnej
  %S - sekundy jako liczba dziesiętna
  %T* - aktualny czas, odpowiednik %H:%M:%S
  %y - rok jako liczba dwucyfrowa, bez uwzględnienia wieku (00 do 99)
  %Y - rok jako liczba 4-cyfrowa
  %Z - strefa czasowa, nazwa lub skrót
  %% - znak '%'
"""