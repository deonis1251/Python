def print_operation_table(operation, num_rows = 6, num_colums = 6):
    if num_colums < 2 or num_rows < 2:
        print("Введите другую размерноость таблицы!")
    else:
        print(' '.join([str(i) for i in range(1, num_colums + 1)]))
        for i in range(2, num_rows + 1):
            print(i, end='   ')
            for j in range(2, num_colums + 1):
                print(operation(i, j), end='  ')
            print()

print_operation_table(lambda x, y: x + y)