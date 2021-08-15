a, b = map(int, input().split())

if a % 2 == 1:
    num1 = a//2 + 1
else:
    num1 = a*5

if b % 2 == 1:
    num2 = b//2 + 1
else:
    num2 = b*5

sum = num1 + num2

print(sum)