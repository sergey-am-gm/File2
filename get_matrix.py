def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_1 = []
        for j in range(m):
            matrix_1.append(value)
        matrix.append(matrix_1)
    return matrix

# или без вложенных циклов
def get_matrix1(n, m, value):
    matrix_1 = []
    for j in range(m):
        matrix_1.append(value)
    matrix = []
    for i in range(n):
        matrix.append(matrix_1)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)