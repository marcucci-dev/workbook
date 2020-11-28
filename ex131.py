import ex096
import ex097


def infix_to_postfix(infix_expr):
    """Exercise 131: Infix to Postfix
    """
    operators_list = list()
    postfix_list = list()
    for token in infix_expr:
        if ex096.isinteger(token):
            postfix_list.append(token)
        elif token in "+-*/^":
            while operators_list != [] \
                    and operators_list[-1] != "(" \
                    and ex097.precedence(token) < ex097.precedence(operators_list[-1]):
                # Remove the last item from operators and append it to postfix
                last_op = operators_list.pop()
                postfix_list.append(last_op)
            operators_list.append(token)

        # If the token is an open parenthesis then
        elif token == '(':
            operators_list.append(token)
        elif token == ')':
            while operators_list[-1] != "(":
                last_op = operators_list.pop()
                postfix_list.append(last_op)
            # Remove the open parenthesis from operators
            operators_list.pop()  # remove '('
    while operators_list:  # != []
        last_op = operators_list.pop()
        postfix_list.append(last_op)
    return postfix_list


res = infix_to_postfix(['(', '1', '+', '2', ')', '-', '(', '3', '*', '4', ')'])
print(res)
