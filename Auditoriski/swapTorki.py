def swap(lista):
    return [[(b, a) for a, b in lista]]


if __name__ == '__main__':
    print(swap([('a', 1), ('b', 2), ('c', 3)]))
