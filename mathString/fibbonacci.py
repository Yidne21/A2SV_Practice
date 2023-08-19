n = int(input())
answer = []
if n == 1:
    answer = [0]
elif n == 2:
    answer = [0, 1]
else:
    answer = [0, 1]
    i = 2
    while i < n:
        answer.append(answer[-2] + answer[-1])
        i += 1
print(answer)
