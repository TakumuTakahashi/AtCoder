n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
x -= sum(m)
mini = min(m)
print(n + x//mini) # //は切り捨て除算
