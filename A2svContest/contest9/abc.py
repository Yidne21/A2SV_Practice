from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    count = Counter(s)
    if s[0] == s[-1]:
        print('NO')
        continue
    elif abs(count['A'] - count['B']) > count['C'] or \
         abs(count['B'] - count['C']) > count['A'] or \
         abs(count['A'] - count['C']) > count['B']:
        print('NO')
    else:
        print('YES')
