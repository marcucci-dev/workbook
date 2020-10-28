def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return -1

if __name__ == '__main__':
    while True:
        operator = input('Write an operator: ')
        res = precedence(operator)
        if res == -1:
            print('Error: the input is not an operator')
        else:
            print('The precedence of operator is', res)

    operator = '^'
    res = precedence(operator)
    print(res)