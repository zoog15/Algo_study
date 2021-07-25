# julka : https://www.acmicpc.net/problem/8437

total = int(input())  # 사과의 총 갯수
more = int(input())  # 클라우디아가 더 갖고있는 사과의 수

x = (total-more) // 2  # 사과의 갯수는 정수이기때문에 몫만 계산

print(x+more)
print(x)
