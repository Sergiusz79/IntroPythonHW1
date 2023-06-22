'''
Задача 8: 
Требуется определить, можно ли от шоколадки размером n x m долек 
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
'''

try:
    n = int(input("Enter integer number: "))
    m = int(input("Enter integer number: "))
    k = int(input("Enter integer number: "))
except:
    print("Error! This is not integer number!")
else:
    if k % n ==0 or k % m == 0:
        print(f"From a chocolate bar measuring {n} x {m} slices can be break off {k} slices")
    else:
        print(f"From a chocolate bar measuring {n} x {m} slices is impossible break off {k} slices")
