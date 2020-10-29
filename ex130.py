import ex129


def replace_binary_operators(tokens_input):
    tokens_out = []
    for i in range(len(tokens_input)):
        # if tokens_in[i] in "+-":
        is_unary = tokens_input[i] in "+-" and (i == 0 or tokens_input[i - 1] in "+-*/^(")
        token = "u" + tokens_input[i] if is_unary else tokens_input[i]
        tokens_out.append(token)
    return tokens_out


if __name__ == '__main__':
    tokens_in = ['-', '(', '-', '1', '+', '(', '34', '*', '2', '^', '6', ')', '/', '89', ')']
    res = replace_binary_operators(tokens_in)
    print(res)
    assert res == ['u-', '(', 'u-', '1', '+', '(', '34', '*', '2', '^', '6', ')', '/', '89', ')']

    while True:
        expression = input('Write an expression: ')
        res = ex129.tokenize(expression)
        tokens_out = replace_binary_operators(res)
        print('The token list is', tokens_out)