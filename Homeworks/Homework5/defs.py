# Добавляем числа в список пока не 0
def int_while_not_zero(array):
    mark = int(input("Введите оценку: "))
    if mark == 0:
        return array
    array.append(mark)
    array = int_while_not_zero(array)
    return array

# Максимальное значение меняем на минимальное 
def from_max_to_min(array):
    maximum = max(array)
    for el in range(len(array)):
        if array[el] == maximum:
            array[el] = min(array)
    return array

# Массив из чисел;    принимает длину массива
def create_int_array(length_array):
    array = []
    for el in range(length_array):
        num = int(input(f"Введите {el + 1} элемент массива: "))
        array.append(num)
    return array

# Проверка числа (простое или нет)
def prime_num(num):
    delit = 2
    while num % delit != 0: 
        delit += 1
    return delit == num

# Заполнение массива наоборот   int
def rever(lenght):
    nums = []
    for el in range(lenght):
        num = int(input(f"Введите {el + 1} элемент массива: "))
        nums.insert(0, num)
    return nums

# Сумма двух чисел 
def umnojenie_nums(a, b):
    if b == 1:
        return a
    return a * umnojenie_nums(a, b - 1)

# Сумма двух неотрицательных цисел 
def rec_sum(a, b):
    if a == 0:
        return b
    else:
        return rec_sum(a - 1, b + 1)
    
# Количество чисел, которые больше соседних в массиве
def near_min(nums):
    count = 0
    for el in range(len(nums) - 1):
        if nums[el - 1] < nums[el] > nums[el + 1]:
            count += 1
    return count

# 