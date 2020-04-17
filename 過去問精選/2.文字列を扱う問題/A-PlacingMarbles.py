# 入力された文字列の中にある1の数を出力
s = input()
count = 0
for i in s:
    if i == '1':
        count += 1
print(count)

#---別解---
# print(input().count('1'))