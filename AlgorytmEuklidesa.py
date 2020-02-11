'''
Program ma za zadanie policzyć NWD dla dwóch podanych liczb i wyświetlić policzone NWD na ekranie.
'''

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if a == b:
    pass
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print("NWD =", a)
