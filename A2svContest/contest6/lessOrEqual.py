def binary_search(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left


n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(map(int, input().split()), reverse=True)

ans = [len(a) - binary_search(a, bi) for bi in b]
print(*ans)
