# days = int(input("Enter days: "))
# minCount = 0
# maxCount = 0
# for i in range(days):
#     temp = int(input("Enter temperature: "))
#     if temp >= 0:
#         maxCount += 1
#     else:
#         minCount += 1
# print(f"Days, when plus temp {maxCount} and days, when minus temp {minCount}")


# list1 = [1, 4, 1, 2, 4, 7]
# num = 6
# raznitsa = [num - i for i in list1]
# print(raznitsa)
# module = [abs(i) for i in raznitsa]
# print(module)
# m = min(module)
# print(m)
# print(num - m)
# # print(num - abs(min(abs(i) for i in [num - i for i in list1])))


# word = 'asd,asdasd, asd  asd, asd, ,aswrfv'
# a = word.split(' ')

# def sum_str(*args):
#     res = int()
#     for i in args:
#         res += i
#     return res

# print(sum_str(1, 2, 3))


# print(list(map(int, [x for x in input("Введите числа через пробел: ").split()])))

# data = [1, 5465, 56, 4, 65, 48, 651, 5, 561, 51, 65, 134, 561, 65]

# print(list(filter(lambda x: x % 2 == 0, data)))

# a = open("t.txt", 'a')
# a.writelines("Привет")
# a.close

# with open("t.txt", 'r') as a:
#     print(a.readline())