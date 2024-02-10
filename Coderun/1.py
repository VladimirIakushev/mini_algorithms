def main():
    '''Средний элемент'''
    a, b, c = map(int, input().split())
    res = sorted([a, b, c])
    print(res[1])


if __name__ == '__main__':
    main()
