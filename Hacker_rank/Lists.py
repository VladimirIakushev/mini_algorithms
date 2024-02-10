N = int(input())
list_output = []
for _ in range(N):
    command = input().split(' ')
#    print(command)
    if str(command[0]) == 'insert':
        list_output.insert(int(command[1]), int(command[2]))
    elif str(command[0]) == 'print':
        print(list_output)
    elif str(command[0]) == 'remove':
        list_output.remove(int(command[1]))
    elif str(command[0]) == 'append':
        list_output.append(int(command[1]))
    elif str(command[0]) == 'sort':
        list_output.sort()
    elif str(command[0]) == 'pop':
        list_output.pop(-1)
    elif str(command[0]) == 'reverse':
        list_output = list_output[::-1]
    else:
        print('The input does not meet the conditions of the task')
