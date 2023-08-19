t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    s = set(a)
    if len(s) == n:
        print(n)
    else:
        if n % 2 == 0:
            print(len(s))
        else:
            print(len(s) - 1)