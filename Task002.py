'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
'''
try:
    s = int(input("Enter number multiple of 4: \n"))
except:
    print("Error! This is not integer number!")
else:
    if s % 4 != 0:
        print("Error! This number is not a multiple of 4!")
    else:
        kat = s//2
        pit = s//4
        print(f"Katya made {kat} cranes. Petya and Serg made {pit} cranes each.")
