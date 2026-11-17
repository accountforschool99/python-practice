M = int(input())

for P in range(M, 0, -1):
    for space in range(M - P):
        print(' ', end='')

    for O in range (P):
        print('1', end='')
        if O < P - 1:
            print('0', end='')
    print()