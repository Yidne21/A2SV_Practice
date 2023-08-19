n = int(input())
b = list(map(int, input().split(' ')))

c25, c50 = 0, 0

for m in b:
    if m == 25:
        c25 += 1
    elif m == 50:
        if c25 > 0:
            c25 -= 1
            c50 += 1
        else:
            print('NO')
            exit()
    elif m == 100:
        if c50 > 0 and c25 > 0:
            c50 -= 1
            c25 -= 1
        elif c25 >= 3:
            c25 -= 3
        else:
            print('NO')
            exit()

print('YES')
