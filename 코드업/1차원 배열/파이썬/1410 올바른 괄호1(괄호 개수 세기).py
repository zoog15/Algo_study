a = list(input())
l = len(a)

cnt1 = 0
cnt2 = 0

for i in range(l):
    b = a.pop()
    if b == '(':
        cnt1 += 1
    if b == ')':
        cnt2 += 1

print(cnt1, cnt2)
