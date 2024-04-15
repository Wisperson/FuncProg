n = int(input())


def recurse_bruh(word, symbol, left_length):
    if (left_length == 0):
        print(word)
        return
    word = word + symbol
    left_count = word.count('(')
    right_count = word.count(')')
    if (left_count > right_count + left_length or right_count > left_count + left_length):
        return
    recurse_bruh(word, '(', left_length - 1)
    recurse_bruh(word, ')', left_length - 1)


recurse_bruh("", '(', n * 2)
