# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def find_outlier(integers):
    odd = []
    even = []
    for el in range(len(integers)):
        if (integers[el] % 2) == 0:
            even.append(integers[el])
        else: 
            odd.append(integers[el])
    
    if len(odd) > len(even):
        return even[0]
    else: return odd[0] 

a = [160, 3, 1719, 19, 11, 13, -21]

print(find_outlier(a))
