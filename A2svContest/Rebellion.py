t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    copy = a.copy()
    copy.sort()
    cnt = 0
    for j in range(n):
        if copy[j] != a[j]:
            cnt += 1
    print(cnt // 2)
