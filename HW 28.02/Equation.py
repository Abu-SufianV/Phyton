#Ax^2+Bx+C=0

import math

A=int(input("Введите переменную А: "))
B=int(input("Введите переменную B: "))
C=int(input("Введите переменную C: "))

print ("\n\nA =", A, "\nB =", B,"\nС =" , C)

D = B*B - 4*A*C
if D>0:
    x1=(-B+math.sqrt(D))/(2*A)
    x2=(-B-math.sqrt(D))/(2*A)
    print("D =", D, "\nПевый корень:", x1, "\nВторой корень: ", x2)
elif D==0:
    x=-B/(2*A)
    print("D =", D, "\nКорень:", x)
else:
    print("Корней нет")
