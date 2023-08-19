t = int(input())

for _ in range(t):
    s = input()
    minlen = len(s) + 1
    counts = [0, 0, 0]
    l = 0

    for r in range(len(s)):
        counts[int(s[r]) - 1] += 1

        while all(counts):
            minlen = min(minlen, r - l + 1)
            counts[int(s[l]) - 1] -= 1
            l += 1

    if minlen == len(s) + 1:
        print(0)
    else:
        print(minlen)
