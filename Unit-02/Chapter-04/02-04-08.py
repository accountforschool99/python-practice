S1 = int(input())
S2 = int(input())
S3 = int(input())

if S1 + S2 > S3 and S1 + S3 > S2 and S2 + S3 > S1:
    if S1 == S2 == S3:
        print('equilateral')
    elif S1 == S2 or S1 == S3 or S2 == S3:
        print('isosceles')
    else:
        print('scalene')
else:
    print('not a triangle')