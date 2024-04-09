def goal_test(state):
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                return False
    return True


if __name__ == '__main__':
    a = (1, 1, 1, 1, 1, 1, 0, 1, 1)
    n = 3
    rows = []
    for i in range(n):
        rows.append(a[i * n: (i + 1) * n])
    rows = tuple(rows)
    print(goal_test(rows))