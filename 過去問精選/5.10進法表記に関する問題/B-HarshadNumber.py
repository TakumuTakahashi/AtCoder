N = int(input())
f_x = sum(map(int, str(N)))
if N % f_x == 0:
    print('Yes')
else:
    print('No')