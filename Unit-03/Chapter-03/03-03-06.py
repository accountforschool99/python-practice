P = int(input())


for P in range(P , 0, -1):
    for O in range (P):
        print('1', end='')
        if O < P - 1:
            print('0', end='')
    print()
    