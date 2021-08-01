# 1978번 소수 찾기 : https://www.acmicpc.net/problem/1978

n = int(input())  # 입력받을 숫자의 갯수
a = list(map(int, input().split()))


cnt2 = 0  # 소수 갯수 세기

for i in a:
    cnt1 = 0  # 약수 갯수 세기
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            cnt1 += 1
    if cnt1 == 1:
        # print(i)
        cnt2 += 1

print(cnt2)

