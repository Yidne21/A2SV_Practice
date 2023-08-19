n = int(input())
m = list(map(int, input().split(' ')))
maxl = 1  
length = 1 

for i in range(1, n):
    if m[i] >= m[i - 1]:
        length += 1
    else:
        maxl = max(maxl, length)
        length = 1

maxl = max(maxl, length) 
print(maxl)
