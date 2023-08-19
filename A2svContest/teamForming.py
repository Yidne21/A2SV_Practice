n = int(input())
s = list(map(int, input().split(' ')))
s.sort()
noOfProblem = 0
jump = 0
for i in range(n):
    if i + 1 + jump < n:
        noOfProblem += s[i + 1 + jump] - s[i + jump]
        jump += 1
print(noOfProblem)