s = input()

while 1:
    for x in ('dream', 'dreamer', 'erase', 'eraser'):
        if s.endswith(x):
            s = s[:-len(x)]
            break
    else:
        print('NO')
        break
    if not s:
        print('YES')
        break