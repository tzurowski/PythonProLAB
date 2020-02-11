# deklaracja i inicjalizacja zmiennych
'''
a = 1           
b = 1.1        
c = "tekst"
d = True
type(a) # sprawdzenie typu danego obiektu
'''

# wyświetlenie danych
'''
print(type(a))
print("Witam moich studentów")
'''

# wprowadzenie danych
'''
name = input("Jak masz na imię: ")
print("Siema", name)
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

# instrukcja warunkowa if
if a > b:
    print("a jest wieksze od b")
elif a < b:
    print("b jest wieksze od a")
else:
    print("a i b są róne")
'''

# pętla for
'''
for i in range(5):
    print(i)
'''

# petla while
'''
i = 0
while i < 5:
    print(i)
    i += 1
'''

# listy
'''
naszaLista = []
print(type(naszaLista))
naszaLista.append(2)     # dodanie do listy dwójki
print(naszaLista)        # wyświetlenie listy
'''
'''
naszaLista = [1, 2, 3.4, "keczup", True]    # nadpisanie wartości listy
naszaLista.append(1)    # dodanie do listy jedynki
print("Zawartość listy po dodaniu jedynki: ", naszaLista)
naszaLista.count(1)  # zlicza jedynki (True == 1)
x = len(naszaLista)  # len(naszaLista) zwraca długość listy
print("Długość naszej listy wynosi: ", x)
naszaLista2 = ["cos", 2, 3, 4]
naszaLista.extend(naszaLista2)  # dodanie do naszaLista listy naszaLista2
print("Nasza lista po dołączeniu drugiej listy: ", naszaLista)
print("Index jedynki = ", naszaLista.index(1))  # pierwszy index jedynki
naszaLista.insert(1, False)  # wstawienie danych (False) przed indexem 1
print("Nasza lista po dodaniu wartości False: ", naszaLista)
naszaLista.remove(1)    # skasowanie pierwszego wystąpienia jedynki
print("Lista ze skasowanym item o wartości 1: ", naszaLista)
naszaLista.reverse()    # odwrócenie listy
print("Lista po odwróceniu kolejności: ", naszaLista)
naszaLista.clear()  # skasowanie zawartości listy
print("Lista po skasowaniu zawartości: ", naszaLista)
'''

'''
lista = [2, 1, 34, 2]
print("Lista przed posortowaniem: ", lista)
lista.sort()    # sortowanie listy
print("Posortowana lista: ", lista)
lista2d = [[1, 2, 3], [4, 5]]
print("Zawartość listy 2D o indexie 0,2: ", lista2d[0][2])
print("Zawartość listy 2D: ", lista2d)

# wypisanie wszystkich elementów listy pętlą
for cos in lista:
    print(cos)
'''

# lista niemodyfikowalna
'''
tup = (1, 2, 3, 4)
print(type(tup))
'''

# lista słownik
'''
slownik = {1: "mąka", 2: "ziew"}  # własne indexowanie
print("Zawartość listy: ", slownik)
print("Indexy listy: ", slownik.keys())
print("Zawartość listy: ", slownik.values())
'''

# zbiory
'''
zbior = set()  # zbior nie może mieć duplikatów
print(type(zbior))
zbior.add(1)    # dodanie 1 do zbioru
print("Nasz zbiór: ",zbior)
'''

# funkcje
'''
def NaszaFunkcja(a):
    print("Użytkownik wywołał funkcję z parametrem równym: ", a)


NaszaFunkcja(10)
NaszaFunkcja("Kot")
NaszaFunkcja(True)
'''
