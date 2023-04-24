song = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
leters = ['а', 'ё', 'е', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = song.split()
if len(phrases) < 2:
    print("Количество фраз должно быть больше одной!")
else:
    count_let = []
    for i in phrases:
        count_let.append(len([x for x in i if x.lower() in leters]))
if set(count_let) == 1:
    print("Парам пам-пам!")
else:
    print("Пам парам!")