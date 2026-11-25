J = int(input())

for row in range(1, J + 1):       
    for column in range(1, J + 1):   
        if column > 1:
            print(' ', end='')
        print(row * column, end='')
    print()