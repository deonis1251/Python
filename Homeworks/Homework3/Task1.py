# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


list = []
lenght = int(input("Enter lenght of array: "))

for i in range(lenght):
    num = int(input(f"Enter {i + 1} number: "))
    list.append(num)
    
values = int(input("What you need: "))
print(list.count(values))