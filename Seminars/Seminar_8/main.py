import interface, funcs

def main_prog():
    flag = True
    while flag:
        a = interface.hello()
        if a == '1':
           funcs.add_contact(interface.get_contact())
        elif a == '2':
            funcs.search_contact()
        elif a == '3':
            funcs.print_all()
        elif a == '4':
            funcs.change_contact(interface.get_change_contact())
        elif a == '5':
            funcs.del_contact(interface.get_del_contact())
        else:
            flag = False

main_prog()
