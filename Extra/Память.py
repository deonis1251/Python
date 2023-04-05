import sys
a = (sys.getsizeof(3**9090001) / (1024 * 1024)) # Сколько памяти занимает "3**9090001" в Мб 
print(round((sys.getsizeof(3**9090001) / (1024 * 1024)), 2))



