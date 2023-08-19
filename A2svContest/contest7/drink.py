def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    return low


ns = int(input())
price = list(map(int, input().split(' ')))
price.sort()

day = int(input())

for i in range(day):
    c = int(input())
    ans = binary_search(price, c)
    print(ans)
