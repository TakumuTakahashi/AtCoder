s = input()
for i in range(len(s)):
    if s[i] == 'A':
        head = i
        break
for i in range(len(s)):
    if s[-(1+i)] == 'Z':
        tail = len(s)-i-1
        break
print(tail - head + 1)