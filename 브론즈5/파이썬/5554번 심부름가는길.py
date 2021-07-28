# 심부름 가는 길 : https://www.acmicpc.net/problem/5554

t = []
total = 0

for i in range(4):
    t.append(int(input()))
    total += t[i]

m = total//60
s = total % 60

print(m)
print(s)

