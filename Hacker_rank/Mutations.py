def mutate_string(string, position, character):
    list_for_change = list(string)
    list_for_change[position] = character
    string = ''.join(list_for_change)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
