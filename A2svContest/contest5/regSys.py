#!/usr/bin/python3
n = int(input())
db = []
count = {}
for i in range(n):
    name = input()
    count[name] = 1 + get(name, 0)
    if name not in db:
        db.append(name)
        print('OK')
    elif name in db:
        newName = name + str(count[name])
        db.append(newName)
        print(newName)

