def max_possible_cost(n, a):
    a.sort()
    colors = 1
    max_cost = 0

    for i in range(1, n):
        gap = a[i] - a[i - 1]

        if gap > 1:
            colors += 1
            max_cost += gap - 1

    return max_cost

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(max_possible_cost(n, a))

