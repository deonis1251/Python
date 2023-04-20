# Прогрессия   an = a1 + (n - 1) * d
def func(first, step, lenght):
    for el in range(lenght):
        num = first + step * el
        print(num, end=' ') 

# Массив из чисел;    принимает длину массива
def create_int_array(length_array):
    array = []
    for el in range(length_array):
        num = int(input(f"Введите {el + 1} элемент массива: "))
        array.append(num)
    return array

# Индексы чисел в диапозоне (мин, макс)
def min_max_in_nums(nums):
    mini = int(input("Введите минимальное значение: "))
    maxi = int(input("Введите максимальное значение: "))
    result = []
    for el in range(len(nums)):
        if mini <= nums[el] <= maxi:
            result.append(el)
    return result