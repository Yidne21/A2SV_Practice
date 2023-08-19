#!/usr/bin/python3

n = int(input())
count = {}

for i in range(n):
    name = input()
    count[name] = count.get(name, 0) + 1

    if count[name] == 1:
        print('OK')
    else:
        newName = name + str(count[name] - 1)
        print(newName)

