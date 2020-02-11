'''
Program polegający na wypisaniu n-tego elementu ciągu fibonacciego używając rekurencji.
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


def fibonacci_rekurencyjnie(n):
    if n <= 1:
        return 1
    elif n <= 2:
        return 1
    else:
        return fibonacci_rekurencyjnie(n-1) + fibonacci_rekurencyjnie(n-2)


print(f"{a} liczbą ciągu Fibonacciego jest: {fibonacci_rekurencyjnie(a)}")
