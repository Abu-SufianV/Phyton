def NOD(x,y):
    while x != 0 and y != 0:
        if x>y:
            x=x%y
        else:
            y=y%x
    return x+y

amount=int(input("Введите количество повторов: "))

while amount != 0:
    first=int(input("\n\nВведите первое число: "))
    second=int(input("Введите второе число: "))
    if first==0 or second==0:
        print("Число не должно быть равно нулю !!!")
    else:
        print("------------------\nНаибольший общий делитель данных чисел равен: ",NOD(first, second))
