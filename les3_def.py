# ФУНКЦИЯ НАХОЖДЕНИЯ МАКСИМУМА 

# def maxim(a, b):
#     if a > b:
#         return a
#     return b

# ЧИСЛА ФИБОНАЧЧИ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n -2)
# # пример
# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)

# СОРТИРОВКА МАССИВА   INT

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10, 5, 7, 28]))

# СОРТИРОВКА МАССИВА   INT

# def quick_sort_my(array):
#     array_2 = []
#     while len(array) > 0:
#         mini = min(array)
#         array.remove(mini)
#         array_2.append(mini)
#     return array_2

# print(quick_sort_my([102, 5, 8, 12, 245, 25, 25.45, 26]))

# СОРТИРОВКА СЛИЯНИЕМ   INT

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
    
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [5,4,8,6,4,8,9,2,4,8,8,4]
# merge_sort(list1)
# print(list1)

