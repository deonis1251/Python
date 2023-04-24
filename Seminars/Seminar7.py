# # Задача 1 
# nums = list(map(int, input("Enter numbers: ").split()))
# result = list(filter(lambda x: 9 < abs(x) < 100, nums))
# print(result)

# # Задача 2 
# nums = list(filter(lambda x: x.isnumeric() , input("Enter number: ")))
# result = list(map(int, nums))
# print(sum(result))

# # Задача 3
# list_1 = [1, 2, 5, '7', '8']
# result_1 = list(filter(lambda x: type(x) is int, list_1))
# result_2 = list(filter(lambda x: type(x) is str, list_1))
# print(result_1, result_2, sep='\n')
