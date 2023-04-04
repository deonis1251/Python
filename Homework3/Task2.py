# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

list = []
lenght = int(input("Enter lenght of array: "))

for i in range(lenght):
    num = int(input(f"Enter {i + 1} number: "))
    list.append(num)

number = int(input("Enter number: "))
min = abs(number - list[0])

for i in range(1, len(list)):
    module = abs(number - list[i])
    if module < min:
        min = module 
        index = i
        
print(list[index])
