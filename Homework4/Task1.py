# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

lot_1 = []
lot_2 = []
long_1 = int(input("Введите длину первого множества: "))
long_2 = int(input("Введите длину второго множества: "))

for el in range(long_1):
    num_1 = int(input(f'Введите {el + 1} элемент первого множества: '))
    lot_1.append(num_1)

print()

for el in range(long_2):
    num_2 = int(input(f'Введите {el + 1} элемент второго множества: '))
    lot_2.append(num_2)

print(set(lot_1).intersection(lot_2))
