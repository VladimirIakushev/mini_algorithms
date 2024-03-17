import textwrap


def wrap(string, max_width):
    result = '\n'.join(textwrap.wrap(string, max_width))
    return str(result)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
