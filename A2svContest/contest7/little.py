n, q = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
hashmap = {}
for _ in range(q):
    l, r = map(int, input().split(' '))
    hashmap[(l, r)] = hashmap.get((l, r), 0) + 1
print(hashmap)

