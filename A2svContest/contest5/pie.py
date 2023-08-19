#!/usr/bin/python3
n = int(input())
_key = {}
ans = 0
st = input()
for i in st:
    if i.islower():
        _key[i.upper()] = _key.get(i.upper(), 0) + 1
    elif i.isupper():
        if i not in _key or _key[i] == 0:
            ans += 1
        elif i in _key and _key[i] > 0:
            _key[i] = _key.get(i) - 1
print(ans)
