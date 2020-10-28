def tokenize(exp):
    token_list = []
    i = 0
    number = ''
    last = len(exp) - 1
    for i in range(len(exp)):
        char = exp[i]
        if char in '+-*/^()':
            token_list.append(char)
#        elif char == ' ':
#            pass
        elif char in '0123456789':
            number += char
            if i == last or exp[i+1] not in '0123456789':
                token_list.append(number)
                number = ''
        i += 1
    return token_list

if __name__ == '__main__':
    while True:
        expression = input('Write an expression: ')
        res = tokenize(expression)
        print('The token list is', res)

    operator = '^'
    res = precedence(operator)
    print(res)