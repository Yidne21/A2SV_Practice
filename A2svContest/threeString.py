t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    # The first character of s2 must be 'A'.
    if s[0] == 'B':
        print("NO")
        continue

    # Check if we can transform s1 into s2
    prev = 0  # index of the last 'B' encountered
    for i in range(1, n):
        if s[i] == 'B':
            # Check if the substring from prev+1 to i-1 is good
            good_len = i - prev - 1
            if good_len == 0 or (good_len > 1 and good_len % 2 == 0):
                print("NO")
                break
            prev = i
    else:
        # Check the last good substring
        good_len = n - prev - 1
        if good_len == 0 or (good_len > 1 and good_len % 2 == 0):
            print("NO")
        else:
            print("YES")
