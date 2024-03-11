import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def calculate_mines(i1, j1, pos):
    result = 0
    for (m1, m2) in pos:
        if m1 == i1 and m2 == j1 - 1:
            result += 1
        if m1 == i1 and m2 == j1 + 1:
            result += 1
        if m2 == j1 and m1 == i1 + 1:
            result += 1
        if m2 == j1 and m1 == i1 - 1:
            result += 1

        if m1 == i1 + 1 and m2 == j1 + 1:
            result += 1
        if m1 == i1 + 1 and m2 == j1 - 1:
            result += 1
        if m1 == i1 - 1 and m2 == j1 - 1:
            result += 1
        if m1 == i1 - 1 and m2 == j1 + 1:
            result += 1
    return result


if __name__ == "__main__":
    size_matrix = int(input())
    rows = []
    for i in range(size_matrix):
        rows.append(input().strip().split())
    matrix = [[cell for cell in row] for row in rows]
    mine_position = []
    for i in range(size_matrix):
        for j in range(size_matrix):
            if matrix[i][j] == '#':
                mine_position.append((i, j))
    for i in range(size_matrix):
        for j in range(size_matrix):
            if matrix[i][j] != '#':
                res = calculate_mines(i, j, mine_position)
                matrix[i][j] = res
    for i in matrix:
        r = "   ".join(str(c) for c in i)
        print(r)
