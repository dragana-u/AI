if __name__ == '__main__':
    n = int(input())
    m = int(input())
    mat = []
    for i in range(0, n):
        elements_row = [int(element) for element in input().split(" ")]
        mat.append(elements_row)
    res = [x * 2 for row in mat for x in row]
    print(res)