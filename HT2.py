# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 


def summa (A,B):
    s = 0
    count1 = 0
    count2 = 0
    if count1 == B & count2 == A: 
        return s
    else :
        if count1 <B:
            count1 +=1
            s =summa (A,B-1)+1
        elif count2  < A:
                count2 +=1
                s =summa (A-1,B)+1
                return s
    return s
        
print (f'Сумма {summa (int(input("Введите 1 число: ")),int(input("Введите 2 число: ")))}')