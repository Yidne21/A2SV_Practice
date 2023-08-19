n = input()
cnt4 = n.count('4')
cnt7 = n.count('7')
tot = cnt4 + cnt7
if tot == 7 or tot == 4:
    print('YES')
else:
    print('NO')
