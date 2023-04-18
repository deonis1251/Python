# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.


coin = int(input("Enter quantity coins: "))
count_0 = 0
count_1 = 0
for i in range(coin):
    side = int(input("Enter side(1 or 0): "))
    if side == 1:
        count_1 += 1
    else: count_0 += 1
if count_0 < count_1:
    print("Flip coins with 0 side!")
else: print("Flip coins with 1 side!")