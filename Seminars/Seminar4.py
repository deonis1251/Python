# stroka = input("Введите строку: ").split()
# stroka_2 = {}

# for i in stroka:
#     if i in stroka_2:
#         print(f'{i}_{stroka_2[i]}', end='\n')
#     else:
#         print(i, end='_1\n')
#     print(stroka_2)
#     stroka_2[i] = stroka_2.get(i, 1) + 1


# a = str(input("Введите строку: "))
# fantom_a = list()
# for el in a:
#     fantom_a.append(el)
#     print(f"{el}_{fantom_a.count(el)}")


# a = [2, 3, 4, 5, 6, 7, 3, 11, 0, 19, 5]
# max = a[0]
# for el in a:
#     if el > max:
#         max = el
#     if el == 0:
#         break
# print(max)

# a = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(len(set(a.upper().split())))