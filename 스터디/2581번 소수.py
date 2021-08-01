# 2581번 소수 : https://www.acmicpc.net/problem/2581

n = int(input())
m = int(input())
sum = 0
flag = 0  # min_n에 제일 작은 소수가 들어갔는지 안들어갔는지 확인용

for i in range(n, m+1):
    cnt = 0
    if i == 1:  # 1은 볼필요 없음
        continue
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break  # 소수가 아님이 판별됐으면 바로 break 하고 넘어가기
    if cnt == 0 and flag == 0:
        min_n = i
        flag += 1
        sum += i
    elif cnt == 0:
        sum += i

if sum == 0:
    print("-1")
else:
    print(sum)
    print(min_n)


