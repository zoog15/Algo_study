import math

money = int(input())
money2 = money
day = int(input())
change = list(map(int, input().split()))
change2 = []

for i in change:
    change2.append(1+(i/100))

for i in change2:
    money2 *= i

differ = money2 - money

print(format(differ, ".0f"))

if differ < 0:
    print("bad")
elif differ == 0:
    print("same")
else:
    print("good")