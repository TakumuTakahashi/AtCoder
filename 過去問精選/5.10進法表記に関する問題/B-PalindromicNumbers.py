A, B = map(int, input().split())
count = 0
for i in range(A, B+1):
    # A以上B以下の数各々に対して
    if str(i)[0]==str(i)[-1] and str(i)[1]==str(i)[-2]:
        count += 1
print(count)