'''
Program polegający na wypisaniu n-tego elementu ciągu fibonacciego używając iteracji.
'''
while True:
    try:
        a = int(input("Podaj numer oczekiwanego elmentu z ciągu Fibonacciego: "))
        if a <= 0:
            raise ValueError
        break
    except ValueError:
        print("Podano błędne dane!")
        continue

F2, F1, i = 1, 1, 2

if a == 1:
    print(f"{a} liczbą ciągu Fibonacciego jest: {F2}")
elif a == 2:
    print(f"{a} liczbą ciągu Fibonacciego jest: {F1}")
else:
    while i < a:
        F2, F1 = F1, F1+F2
        i += 1
    print(f"{a} liczbą ciągu Fibonacciego jest: {F1}")
