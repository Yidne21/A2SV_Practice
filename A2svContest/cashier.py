n, l, a = map(int, input().split(' '))
total = 0
for i in range(n):
    ti, li = map(int, input().split(' '))
    if n >= 2:
        total += li - ti
    else:
        total += li
print((l - total) // a)