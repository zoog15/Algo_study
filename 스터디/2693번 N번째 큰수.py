# 2693번 N번째 큰 수 : https://www.acmicpc.net/problem/2693

n = int(input())  # 테스트 케이스 숫자

while n != 0:
    a = list(map(int, input().split()))
    a.sort(reverse=True)  # 역순으로 정렬
    print(a[2])
    n -= 1






