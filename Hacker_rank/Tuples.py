if __name__ == '__main__':
    ''' Искомый хэш на HackerRank можно получить использую Pypy3'''
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = tuple(integer_list)
    print(hash(t))
