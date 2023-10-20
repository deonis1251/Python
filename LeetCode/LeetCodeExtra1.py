people = ['Ryan', 'Kieran', 'Mark']

def my_friends(list1):
    result = []
    for el in range(len(list1)): 
        if len(list1[el]) == 4:
            result.append(list1[el])
    return result

print(my_friends(people))
