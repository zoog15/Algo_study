import sys

p, q = map(int, sys.stdin.readline().split())  # p : 숫자, q : p의 약수들중 q번째꺼 찾기
a = []  # 약수를 저장할 배열

for i in range(1, p+1):
    if p % i == 0:
        a.append(i)

if len(a) < q:
    answer = 0
else:
    answer = a[q-1]

print(answer)





