def print_formatted(number):
    binary = format(number, 'b')
    width = len(str(binary))

    for num in range(1, number + 1):
        for base in 'doXb':
            print(
                '{0:{width}{base}}'.format(num, base=base, width=width),
                end=' '
                )
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
