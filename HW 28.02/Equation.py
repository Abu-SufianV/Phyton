import math

A = int(input("Введите переменную А: "))
B = int(input("Введите переменную B: "))
C = int(input("Введите переменную C: "))

D = B * B - 4 * A * C

if C == 0 and A==0:
    x=0
    print(x)
elif A == 0 and B == 0:
    print("")
elif A == 0 and B > 0:
    x = -C / B
    print(x)
elif D > 0:
    x1=(-B + math.sqrt(D))/(2 * A)
    x2=(-B - math.sqrt(D))/(2 * A)
    print(x1, x2)
elif D == 0:
    x = -B / (2 * A)
    print(x)
else:
    print("")
