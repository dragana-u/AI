def first_last(l1):
    return [l1[0], l1[-1]]


if __name__ == "__main__":
    list1 = input().strip().replace(" ", "")
    list1 = list(list1)
    list1 = [int(i) for i in list1]  # change input from String to int
    b = first_last(list1)
    print(b)
