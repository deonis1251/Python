def delete_lishnee(file_path):
    
    with open(file_path, 'r') as file:
        name = file.read().splitlines()

    unique_name = list(set(name))

    with open('unique_name.txt', 'w') as file:
        file.write('\n'.join(unique_name))

delete_lishnee('База.txt')