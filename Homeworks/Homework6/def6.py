# Прогрессия   an = a1 + (n - 1) * d
def func(first, step, lenght):
    for el in range(lenght):
        num = first + step * el
        print(num, end=' ') 

# 