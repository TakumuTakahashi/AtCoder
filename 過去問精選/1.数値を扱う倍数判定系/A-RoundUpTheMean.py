import math # mathモジュールをimportする
a, b = map(int, input().split())
x = (a+b)/2
print(math.ceil(x)) # 切り上げにはceil関数を用いる