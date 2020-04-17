# スペース区切りの整数の入力
a, b = map(int, input().split())
# 積が奇数なら'Odd',偶数なら'Even'と出力
if a*b % 2 != 0:
    print('Odd')
else:
    print('Even')
#---別解---
# print('Even' if a*b % 2 == 0 else 'Odd')