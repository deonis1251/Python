from funcs import *
from interface import *

def main_prog():
    flag = True
    while flag:
        num = start()
        if num == 1:
            add_contact(get_contact())
        elif num == 2:
            search_countact()
        elif num == 3:
            all_contacts()
        else:
            flag = False

main_prog()