operators = ['+', '-', '/', '//', '*', '**', '%']


def calc(num1, op, num2):
    if op in operators:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num2 - num1
        elif op == '/':
            return num1 / num2
        elif op == '//':
            return num2 / num1
        elif op == '*':
            return num1 * num2
        elif op == '**':
            return num1 ** num2
        else:
            return num1 % num2

    else:
        print('Invalid operator')


if __name__ == "__main__":
    op1 = float(input())
    operator = input()
    op2 = float(input())
    res = calc(op1, operator, op2)
    if res is not None:
        print(f'The result of {op1} {operator} {op2} is {res}')

