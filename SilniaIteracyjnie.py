'''
Program ma za zadanie policzyć w sposób iteracyjny silnię liczby wprowadzonej przez użytkownika.
'''

liczba = int(input("Podaj n: "))
wynik = 1

if liczba == 0:
    print("n! = ", wynik)
else:
    while liczba > 0:
        wynik *= liczba
        liczba -= 1
    print("n! =", wynik)
