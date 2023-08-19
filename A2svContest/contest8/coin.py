from collections import Counter


n = int(input())
c = list(map(int, input().split(' ')))
freq = Counter(c)

print(max(freq.values()))
