def add_contact(contact):
    with open('Seminars/Seminar_8/text.txt', "a") as data:
        data.writelines(contact)
        data.write("\n")

def all_contacts():
    contact_list = open('Seminars/Seminar_8/text.txt', 'r')
    num = 1
    for el in contact_list:
        print(f'{num}. {el}')
        num += 1
    contact_list.close()

def search_countact():
    contact_list = open('Seminars/Seminar_8/text.txt', 'r')
    search = input("Введите фамилию для поиска: ").title()
    for el in contact_list:
        if search in el:
            print(el)
    contact_list.close()

