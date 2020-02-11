'''
Program ma za zadanie sprawdzić czy podane typy uzytkownika zgadzają się z liczbami wylosowanymi w losowaniu Lotto. Wyświetlone ma zostać ilść trafionych typów oraz ich wartość.
'''

import random as rand

wylosowane = []
i = 0
doJakiej = 49

while i < 6:
    liczba = rand.randint(1, doJakiej)
    if wylosowane.count(liczba) == 0:
        wylosowane.append(liczba)
        i += 1

podane = set()
i = 0
while i < 6:
    try:
        typ = int(input("Podaj swój typ: {} \n".format(i+1)))
    except ValueError:
        print("Błędne dane!!!")
        continue
    if 0 < typ <= doJakiej and typ not in podane:
        podane.add(typ)
        i += 1

trafione = set(wylosowane) & podane
if trafione:
    print(f"Trafiłeś {len(trafione)} liczb")
    print(trafione)
else:
    print("Nic nie trafiłeś :(")
