# "abcde" -> 0 no characters repeats more than once
# "aabbcde" -> 2  'a' and 'b'
# "aabBcde" -> 2 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1  'i' occurs six times
# "Indivisibilities" -> 2  'i' occurs seven times and 's' occurs twice
# "aA11" -> 2  'a' and '1'
# "ABBA" -> 2  'A' and 'B' each occur twice

def duplicate_count(text):
    result_list = []
    text = text.lower()
    for el in range(len(text)):
        if text.count(text[el]) > 1:
            result_list.append(text[el])
    return len(set(result_list))
    # Your code goes here

print(duplicate_count("indivisibility"))