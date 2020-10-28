def isinteger(word):
    w = word.strip()
    if w[0] == '+' or w[0] == '-':
        w = w[1:]
    for char in w:
        if char not in '0123456789':
            return False
    return True


if __name__ == '__main__':
    number = ' *123 '
    res = isinteger(number)
    print(res)

    number = ' +123 '
    res = isinteger(number)
    print(res)

    number = ' -123 '
    res = isinteger(number)
    print(res)