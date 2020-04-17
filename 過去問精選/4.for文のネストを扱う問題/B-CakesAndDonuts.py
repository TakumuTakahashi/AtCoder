N = int(input())
cake = 4
donut = 7
ac = False
for i in range(25):
    for j in range(14):
        if N == (cake*i + donut*j):
            ac = True
            break
if ac:
    print('Yes')
else:
    print('No')