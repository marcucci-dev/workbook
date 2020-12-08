"""This module contains a code example related to

The Python Workbook, 2nd Edition
by Ben Stephenson

Copyright 2020 Giuseppe Marcucci

License: http://creativecommons.org/licenses/by/4.0/
"""


def are_six_vowels_in_order_old(word):
    """
    Return True if word meets the criteria:
        contains each of the vowels A, E, I, O, U and Y exactly once and in order.
        :param word:
        :return: bool
    """
    vowels = "AEIOUY"
    vowels_found = {}
    word = word.upper()
    index = 0
    for char in word:
        if char in vowels:
            if index >= len(vowels):
                return False
            if char != vowels[index]:
                return False
            else:
                index += 1
            vowels_found[char] = vowels_found.setdefault(char, 0) + 1
            if vowels_found[char] > 1:
                return False
    return all(letter in word for letter in 'AEIOUY')


def are_six_vowels_in_order(word):
    """Input: word

    Return bool True if word meets the criteria:
        contains each of the vowels A, E, I, O, U and Y exactly once and in order.
    """
    word = word.upper()
    vowels = "AEIOUY"
    word_vowels_only = ''
    for char in word:
        if char in vowels:
            word_vowels_only += char
    return word_vowels_only == vowels


def six_vowels_in_order():
    """
    :return: list of words that meet the constraint
    """
    file_name: str = input("Insert file name:")
    # file_name = 'data/for_ex172.txt'
    try:
        fin = open(file_name)
    except FileNotFoundError:
        # Display an error message and quit if the file was not opened successfully
        print("{} could not be opened. Quitting...".format(file_name))
        quit()

    words_found = []
    for row in fin:
        word = row.strip()
        if are_six_vowels_in_order(word):
            words_found.append(word)
    return words_found


def show_words(words):
    # displays the words in list
    if len(words) > 0:
        print("The following {} words meet the criterion:".format(len(words)))
        for w in words:
            print(w)
    else:
        print("Sorry, no word meets the criterion.")


def test():
    assert are_six_vowels_in_order("AEIOUY")
    assert not are_six_vowels_in_order("AAEIOUY")
    assert are_six_vowels_in_order("ABEIOUY")
    assert not are_six_vowels_in_order("AEIOUYY")
    assert not are_six_vowels_in_order("AIOUY")
    assert not are_six_vowels_in_order("")
    assert are_six_vowels_in_order("aeiouy")
    assert not are_six_vowels_in_order("yaeiou")
    assert are_six_vowels_in_order("bbaccdeziwottuzzyqwr")


if __name__ == '__main__':
    words_found = six_vowels_in_order()
    show_words(words_found)

    test()
