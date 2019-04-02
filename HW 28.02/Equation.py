import math

A = int(input("Enter variable A: "))
B = int(input("Enter variable B: "))
C = int(input("Enter variable C: "))

D = B * B - 4 * A * C

if C == 0 and A == 0:
    X = 0
    print(X)
elif A == 0 and B == 0:
    print("")
elif A == 0 and B > 0:
    X = -C / B
    print(X)
elif D > 0:
    X1 = (-B + math.sqrt(D)) / (2 * A)
    X2 = (-B - math.sqrt(D)) / (2 * A)
    print(X1, X2)
elif D == 0:
    X = -B / (2 * A)
    print(X)
else:
    print("")
