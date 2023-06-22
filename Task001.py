# Задача 2: Найдите сумму цифр трехзначного числа.

try:
    n = int(input("Enter integer number: \n"))
except:
    print("Error! This is not integer number!")
else:
    sn = str(n)
    sum = int(sn[0]) + int(sn[1]) + int(sn[2])
    print(f"{sn[0]} + {sn[1]} + {sn[2]} = {sum}")
