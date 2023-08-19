t = int(input())
for i in range(t):
    w, et, ef = map(int, input().split(' '))
    if et * ef < w:
        print(et * ef + 4 * et)
    else:
        print(w * ef + 4)
