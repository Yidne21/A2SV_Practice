n = int(input())
bars = list(map(int, input().split()))

alice = 0
bob = 0
l = 0
r = n - 1

while l <= r:
    if alice <= bob:
        alice += bars[l]
        l += 1
    else:
        bob += bars[r]
        r -= 1

print(l, n - l)
