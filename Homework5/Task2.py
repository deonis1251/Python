# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

num_1 = int(input("Введите первое неотрицительное число "))
num_2 = int(input("Введите второе неотрицательно число "))


def rec_sum(a, b):
    if a == 0:
        return b
    else:
        return rec_sum(a - 1, b + 1)


print(rec_sum(num_1, num_2))