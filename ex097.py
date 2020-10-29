def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return -1


if __name__ == '__main__':
    operator = '^'
    res = precedence(operator)
    print(res)
    assert res == 3

    while True:
        operator = input('Write an operator: ')
        res = precedence(operator)
        if res == -1:
            print('Error: the input is not an operator')
        else:
            print('The precedence of operator is', res)
