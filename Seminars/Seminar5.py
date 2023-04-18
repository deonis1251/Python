import defs 
# # Задача 1
# list_1 = []
# print(defs.from_max_to_min(defs.int_while_not_zero(list_1)))

# # Задача 2
# num = int(input("Введите число: "))
# print(defs.prime_num(num))

# # Задача 3
# lenght = int(input("Введите длину массива: "))
# print(defs.rever(lenght))

lenght = int(input("Введите длину массива: "))
nums = []
def rev(nums, lenght):
    num = int(input("Введите число: "))
    if 1 > lenght:
        return nums
    nums.insert(0, num)
    print(nums)
    rev(nums, lenght - 1)
    


print(rev(nums, lenght))