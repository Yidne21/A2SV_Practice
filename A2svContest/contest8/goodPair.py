n = int(input())
t = list(map(int, input().split()))
s = list(map(int, input().split()))

tg = [0] * n
sg = [0] * n

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if t[i] + t[j] > s[i] + s[j]:
            tg[i] += 1
            sg[j] += 1

gp = 0
for i in range(n):
    gp += tg[i] * sg[i]

print(gp)
