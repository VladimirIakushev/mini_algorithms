import textwrap


def painting(N, M):
    string = ''
    for n in range(1, (N // 2 + 1)):
        for m in range(1, (M + 1)):

            if (m < ((M // 2 + 1) - (3 * (2 * n - 1)) // 2)):
                string = string + '-'
            elif m == (M // 2 + 1) - (3 * (2 * n - 1)) // 2:
                string = string + ('.|.' * (2 * n - 1))
            elif (m >= ((M // 2 + 1) - (3 * (2 * n - 1)) // 2)) and (m < ((M // 2 + 1) + (3 * (2 * n - 1)) // 2) + 1):
                string = string
            elif (m >= ((M // 2 + 1) + (3 * (2 * n - 1)) // 2) + 1):
                string = string + '-'
    for m in range(1, (M + 1)):

        if m < (M // 2 - 2):
            string = string + '-'
        elif m == (M // 2 - 2):
            string = string + 'WELCOME'
        elif m >= (M // 2 - 2) and m < (M // 2 + 5):
            pass
        elif m >= (M // 2 + 5):
            string = string + '-'

    for n in range((N // 2), 0, -1):
        for m in range(1, (M + 1)):

            if (m < ((M // 2 + 1) - (3 * (2 * n - 1)) // 2)):
                string = string + '-'
            elif m == (M // 2 + 1) - (3 * (2 * n - 1)) // 2:
                string = string + ('.|.' * (2 * n - 1))
            elif (m >= ((M // 2 + 1) - (3 * (2 * n - 1)) // 2)) and (m < ((M // 2 + 1) + (3 * (2 * n - 1)) // 2) + 1):
                string = string
            elif (m >= ((M // 2 + 1) + (3 * (2 * n - 1)) // 2) + 1):
                string = string + '-'

    result = textwrap.fill(string, M, break_on_hyphens=False)
    return result


if __name__ == '__main__':
    N, M = input().split()
    N = int(N)
    M = int(M)
    result = painting(N, M)
    print(result)
