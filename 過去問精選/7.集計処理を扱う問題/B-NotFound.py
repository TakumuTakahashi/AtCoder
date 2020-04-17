s = list(input())
flag = True
# ord(文字) == 文字を表す整数(ASCIIコード)
# chr(整数) == 整数に対応する文字
for i in range(ord('a'), ord('z') + 1):
    if s.count(chr(i)) == 0:
        flag = False
        ans = chr(i)
        break
print('None' if flag else ans)