def soma():
    print("Enter size of first matrix:")
    row_column_a = str(input()).split(" ")
    matrix_a = []
    print("Enter first matrix:")
    for x in range(int(row_column_a[0])):
        matrix_a.append(str(input()).split())
    print("Enter size of second matrix:")
    row_column_b = str(input()).split(" ")
    matrix_b = []
    print("Enter second matrix:")
    for x in range(int(row_column_b[0])):
        matrix_b.append(str(input()).split())
    if (row_column_a[0] != row_column_b[0]) or (row_column_a[1] != row_column_b[1]):
        print("\nThe operation cannot be performed.\n")
    else:
        matrix_final = []
        for x in range(int(row_column_a[0])):
            matrix_final.append([])
            for y in range(int(row_column_a[1])):
                matrix_final[x].append(float(matrix_a[x][y]) + float(matrix_b[x][y]))
        print("The result is:")
        for x in range(int(row_column_a[0])):
            linha_impressao = ""
            for y in range(int(row_column_a[1])):
                if y == 0:
                    linha_impressao += str(matrix_final[x][y])
                else:
                    linha_impressao += " " + str(matrix_final[x][y])
            print(linha_impressao)


def mulplica_por_constante():
    print("Enter size of matrix:")
    row_column = str(input()).split(" ")
    matrix = []
    print("Enter first matrix:")
    for x in range(int(row_column[0])):
        matrix.append(str(input()).split())
    print("Enter constant:")
    constante = int(input())
    matrix_final = []
    for x in range(int(row_column[0])):
        matrix_final.append([])
        for y in range(int(row_column[1])):
            matrix_final[x].append(float(matrix[x][y]) * constante)
    print("The result is:")
    for x in range(int(row_column[0])):
        linha_impressao = ""
        for y in range(int(row_column[1])):
            if y == 0:
                linha_impressao += str(matrix_final[x][y])
            else:
                linha_impressao += " " + str(matrix_final[x][y])
        print(linha_impressao)


def mulplica_matrizes():
    print("Enter size of first matrix:")
    row_column_a = str(input()).split(" ")
    matrix_a = []
    print("Enter first matrix:")
    for x in range(int(row_column_a[0])):
        matrix_a.append(str(input()).split())
    print("Enter size of second matrix:")
    row_column_b = str(input()).split(" ")
    matrix_b = []
    print("Enter second matrix:")
    for x in range(int(row_column_b[0])):
        matrix_b.append(str(input()).split())

    ans = ''
    result = [[0 for i in range(100)]
              for j in range(100)]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            result[i][j] = 0
            for k in range(len(matrix_b)):
                result[i][j] = result[i][j] + round(float(matrix_a[i][k]) * float(matrix_b[k][j]), 2)

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            ans = ans + ' ' + str(result[i][j])
        s = ans + ","
        s = s.replace(" ,", "\n")
        ans = s + '\n'
    ans = ans.replace(",", "")
    print("The result is:")
    print(ans)


def transposta_diagonal_principal():
    print("Enter size of matrix:")
    row_column = str(input()).split(" ")
    matrix = []
    print("Enter first matrix:")
    for x in range(int(row_column[0])):
        matrix.append(str(input()).split())
    matrix_final = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("The result is:")
    for x in range(int(row_column[0])):
        linha_impressao = ""
        for y in range(int(row_column[1])):
            if y == 0:
                linha_impressao += str(matrix_final[x][y])
            else:
                linha_impressao += " " + str(matrix_final[x][y])
        print(linha_impressao)


def transposta_diagonal_secundaria():
    print("Enter size of matrix:")
    row_column = str(input()).split(" ")
    matrix = []
    print("Enter matrix:")
    for x in range(int(row_column[0])):
        matrix.append(str(input()).split())
    matrix_final = []
    matrix_aux = []
    for i in range(len(matrix)):
        matrix_aux.clear()
        for j in range(len(matrix[0])):
            matrix_aux.append(matrix[len(matrix[0]) - j - 1][len(matrix[0]) - i - 1])
        matrix_final.insert(i, matrix_aux.copy())
    print("The result is:")
    for x in range(int(row_column[0])):
        linha_impressao = ""
        for y in range(int(row_column[1])):
            if y == 0:
                linha_impressao += str(matrix_final[x][y])
            else:
                linha_impressao += " " + str(matrix_final[x][y])
        print(linha_impressao)


def transposta_vertical():
    print("Enter size of matrix:")
    row_column = str(input()).split(" ")
    matrix = []
    print("Enter matrix:")
    for x in range(int(row_column[0])):
        matrix.append(str(input()).split())

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if float(matrix[i][j]).is_integer():
                matrix[i][j] = round(float(matrix[i][j]))
    matrix_final = []
    for j in range(len(matrix[0])):
        matrix[j].reverse()
        matrix_final.append(matrix[j])
    print("The result is:")
    for x in range(int(row_column[0])):
        linha_impressao = ""
        for y in range(int(row_column[1])):
            if y == 0:
                linha_impressao += str(matrix_final[x][y])
            else:
                linha_impressao += " " + str(matrix_final[x][y])
        print(linha_impressao)


def transposta_horizontal():
    print("Enter size of matrix:")
    row_column = str(input()).split(" ")
    matrix = []
    print("Enter matrix:")
    for x in range(int(row_column[0])):
        matrix.append(str(input()).split())
    matrix.reverse()
    matrix_final = matrix
    print("The result is:")
    for x in range(int(row_column[0])):
        linha_impressao = ""
        for y in range(int(row_column[1])):
            if y == 0:
                linha_impressao += str(matrix_final[x][y])
            else:
                linha_impressao += " " + str(matrix_final[x][y])
        print(linha_impressao)


def matriz_transposta_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    print("Your choice:")
    acao = int(input())
    if acao == 1:
        transposta_diagonal_principal()
    elif acao == 2:
        transposta_diagonal_secundaria()
    elif acao == 3:
        transposta_vertical()
    elif acao == 4:
        transposta_horizontal()


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def copy_matrix(M):
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 2: Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)

    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC


def determinant_recursive(matrix, total=0):
    # Section 1: store indices in list for row referencing
    indices = list(range(len(matrix)))

    # Section 2: when at 2x2 submatrices recursive calls end
    if len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val

    # Section 3: define submatrix for focus column and
    #      call this function
    for fc in indices:  # A) for each focus column, ...
        # find the submatrix ...
        As = copy_matrix(matrix)  # B) make a copy, and ...
        As = As[1:]  # ... C) remove the first row
        height = len(As)  # D)

        for i in range(height):
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)  # F)
        # G) pass submatrix recursively
        sub_det = determinant_recursive(As)
        # H) total all returns from recursion
        total += sign * matrix[0][fc] * sub_det

    return total


def calcula_determinante():
    print("Enter size of matrix:")
    row_column = str(input()).split(" ")
    matrix = []
    print("Enter matrix:")
    for x in range(int(row_column[0])):
        matrix.append(str(input()).split())
    for x in range(int(row_column[0])):
        for y in range(int(row_column[1])):
            if float(matrix[x][y]).is_integer():
                matrix[x][y] = round(float(matrix[x][y]))
            else:
                matrix[x][y] = float(matrix[x][y])
    if row_column[0] == "1" and row_column[1] == "1":
        print(matrix[0][0])
    else:
        determinante = determinant_recursive(matrix)
        print(determinante)


def inversa():
    print("Enter size of matrix:")
    row_column = str(input()).split(" ")
    matrix = []
    print("Enter matrix:")
    for x in range(int(row_column[0])):
        matrix.append(str(input()).split())
    for x in range(int(row_column[0])):
        for y in range(int(row_column[1])):
            if float(matrix[x][y]).is_integer():
                matrix[x][y] = round(float(matrix[x][y]))
            else:
                matrix[x][y] = float(matrix[x][y])
    if len(matrix) != len(matrix[0]):
        print("Error")
    elif len(matrix) == 2:
        determinante = determinant_recursive(matrix)
        matrix_final = [[matrix[1][1] / determinante, -1 * matrix[0][1] / determinante],
                        [-1 * matrix[1][0] / determinante, matrix[0][0] / determinante]]
        print("The result is:")
        for x in range(int(row_column[0])):
            linha_impressao = ""
            for y in range(int(row_column[1])):
                if y == 0:
                    linha_impressao += str(matrix_final[x][y])
                else:
                    linha_impressao += " " + str(matrix_final[x][y])
            print(linha_impressao)
    else:
        determinante = determinant_recursive(matrix)
        if determinante != 0:
            matrix_1 = cofactorMatrix(matrix)
            matrix_aux = [[matrix_1[j][i] for j in range(len(matrix_1))] for i in range(len(matrix_1[0]))]
            matrix_final = []
            for x in range(int(row_column[0])):
                matrix_final.append([])
                for y in range(int(row_column[1])):
                    valor = float(matrix_aux[x][y]) * (1 / determinante)
                    if not valor.is_integer():
                        valor = valor * 100
                        valor = int(valor)
                        valor = round(valor / 100, 2)

                    matrix_final[x].append(valor)
            print("The result is:")
            for x in range(int(row_column[0])):
                linha_impressao = ""
                for y in range(int(row_column[1])):
                    if y == 0:
                        linha_impressao += str(matrix_final[x][y])
                    else:
                        linha_impressao += " " + str(matrix_final[x][y])
                print(linha_impressao)


def cofactorMatrix(matrix):
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            matrix_aux = minor(matrix, r, c)
            cofactorRow.append(((-1) ** (r + c)) * determinant_recursive(matrix_aux))
        cofactors.append(cofactorRow)
    return cofactors


def minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    print("Your choice:")
    acao = int(input())
    while acao != 0:
        if acao == 1:
            soma()
        elif acao == 2:
            mulplica_por_constante()
        elif acao == 3:
            mulplica_matrizes()
        elif acao == 4:
            matriz_transposta_menu()
        elif acao == 5:
            calcula_determinante()
        elif acao == 6:
            inversa()
        elif acao == 0:
            exit()
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        print("Your choice:")
        acao = int(input())


menu()
