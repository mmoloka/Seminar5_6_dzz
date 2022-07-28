# Напишите функцию print_operations_table(operation, num_rows=9, num_columns=9), которая принимает в качестве аргументов
# функцию (вычисляющую элемент бинарной операцией - умножение,сложение,возведение в степень, по номеру строки и столбца), 
# аргументы num_rows и num_columns указывают число строк и столбцов таблицы (нумерация идет с единицы), которые должны 
# быть распечатаны.  

def print_operations_table(operation, num_rows, num_columns):
    arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(num_rows):
        for j in range(num_columns):
            arr[0][j] = j + 1
            arr[i][0] = i + 1 
            arr[i][j] = operation(i + 1, j + 1)
    for k in arr:
        print(*list(filter(lambda x: x != 0, k)))

operation_1 = lambda x, y: x * y
operation_2 = lambda x, y: x + y
operation_3 = lambda x, y: x ** y

num_rows = 7
num_columns = 4

print_operations_table(operation_3, num_rows, num_columns)
