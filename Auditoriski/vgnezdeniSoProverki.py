def check(indx, num, elem):
    if indx < num / 2:
        return elem * 3
    else:
        return elem * 2


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    mat = []
    for i in range(0, n):
        elem_row = [int(el) for el in input().split(" ")]
        mat.append(elem_row)
    index = 0
    res = [check(n, i, mat[i][j]) for i in range(0, n) for j in range(0, m)]
    print(res)
