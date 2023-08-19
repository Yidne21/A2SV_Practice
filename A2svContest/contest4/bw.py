t = int(input())

for _ in range(t):
    n, k = map(int, input().split(' '))
    st = input()

    if k == 1:
        if 'B' not in st:
            print(1)
        else:
            print(0)
        continue

    ans = float('inf')
    windowCount = st[:k].count('W')
    ans = min(ans, windowCount)

    for i in range(k, n):
        if st[i - k] == 'W':
            windowCount -= 1
        if st[i] == 'W':
            windowCount += 1
        ans = min(ans, windowCount)

    print(ans)
