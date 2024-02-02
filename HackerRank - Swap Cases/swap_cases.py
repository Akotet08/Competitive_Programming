def swap_case(s):
    n_s = ''
    for letter in s:
        if letter.isupper():
            n_s += letter.lower()
        else:
            n_s += letter.upper()
    return n_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)