# # # # # # # # # # # Задание 1
# def create_int_array(length_array):
#     array = []
#     for el in range(length_array):
#         num = int(input(f"Введите {el + 1} элемент массива: "))
#         array.append(num)
#     return array
#     print()

# def sem6_task1(array_1, array_2):
#     result = []
#     for el in range(len(array_1)):
#         if array_1[el] not in array_2:
#             result.append(array_1[el])
#     return result

# lenght_1 = int(input("Введите длину первого массива: "))
# lenght_2 = int(input("Введите длину второго массива: "))

# nums_1 = create_int_array(lenght_1)
# nums_2 = create_int_array(lenght_2)

# print(sem6_task1(nums_1, nums_2))


# # # # # # # # # # # Задание 2
# def create_int_array(length_array):
#     array = []
#     for el in range(length_array):
#         num = int(input(f"Введите {el + 1} элемент массива: "))
#         array.append(num)
#     return array

# def near_min(nums):
#     count = 0
#     for el in range(len(nums) - 1):
#         if nums[el - 1] < nums[el] > nums[el + 1]:
#             count += 1
#     return count

# print(near_min(create_int_array(int(input("Введите длину массива: ")))))

# # # # # # # # # # # Задача 3
# def create_int_array(length_array):
#     array = []
#     for el in range(length_array):
#         num = int(input(f"Введите {el + 1} элемент массива: "))
#         array.append(num)
#     return array

# def count_couple(nums):
#     count = 0
#     for el in range(len(nums)):
#         for elem in range(el + 1, len(nums)):
#             if nums[el] == nums[elem]:
#                 count += 1
#     return count

# print(count_couple(create_int_array(int(input("Введите длину массива: ")))))

# # # # # # # # # # # Задача 4
# def sum_del(num):
#     sum = 0
#     for el in range(1, num // 2 + 1):
#         if num % el == 0:
#             sum += el
#     return sum

# def sd_to_num(num):
#     for el in range(num):
#         elem = sum_del(el)
#         if sum_del(elem) == el and el < elem:
#             print(el, elem)

# sd_to_num(int(input("Введите число: ")))

