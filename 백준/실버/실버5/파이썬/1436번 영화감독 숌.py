# 1436번 영화감독 숌 : https://www.acmicpc.net/problem/1436
n = int(input())  # 몇번째 종말의 숫자

start = 665
count = 0  # 현재가 몇번째 영화인지 체크하는 카운트

while True:  # count가 n과 같아지면 종료
    start += 1
    s = str(start)

    if "666" in s:
        count += 1
    if count == n:
        break

print(start)