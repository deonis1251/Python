my_dict = dict()
long_dict = int(input("Enter long of dict: "))

for el in range(long_dict):
    key = input(f"Add key number {el+1}: ")
    val = input(f"Add valuem number {el+1}: ")
    try: 
        key = int(key)
        val = int(val)
    except: pass
    my_dict[key] = val
    
print(my_dict)