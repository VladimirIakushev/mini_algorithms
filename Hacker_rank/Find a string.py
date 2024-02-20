'''https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true'''


def count_substring(string, sub_string):
    res = 0
    for i in range(0, len(string)):
        index = string.find(sub_string, i)
        if index != -1 and i >= index:
            res = res + 1
    return res


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
