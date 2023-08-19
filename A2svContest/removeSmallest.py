import math


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    a.sort()
    isNo = False
    if len(a) == 1:
        print('YES')
    else:
        for j in range(0, n):
            if n > j + 1:
                diff = abs( a[j] - a[j + 1])
                if diff > 1:
                    isNo = True
                    break
                else:
                    continue
        if isNo:
            print('NO')
        else:
            print('YES')