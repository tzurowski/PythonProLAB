'''
Program ma za zadanie policzyć w sposób rekurencyjny silnię liczby wprowadzonej przez użytkownika.
'''


def silnia(n=0):
    if n == 1 or n == 0:
        return 1
    else:
        return n*silnia(n-1)


n = int(input("Podaj n: "))
print("n! =", silnia(n))
