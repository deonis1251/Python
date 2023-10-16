def spin_words(sentence):
    list1 = sentence.split()
    list2 = []
    for el in list1:
        if len(el) > 4:
            el = ''.join(reversed(el))
            list2.append(el)
        else: list2.append(el)
    return ' '.join(list2)

print(spin_words('Hey fellow warriors'))
