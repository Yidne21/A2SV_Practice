s = input()
hello = "hello"
idx = 0

for char in s:
    if char == hello[idx]:
        idx += 1
        if idx == len(hello):
            print('YES')
            break

if idx < len(hello):
    print('NO')
