a = list(map(int,input().split()))

sum = 0

for i in a :
    sum += i**2

result = sum%10

print(result)
