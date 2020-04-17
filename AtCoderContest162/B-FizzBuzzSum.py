N = int(input())

count = 0
for i in range(N+1):
    if i % 15 == 0:
        i = 'FizzBuzz'
    elif i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    else:
        count += i
print(count)