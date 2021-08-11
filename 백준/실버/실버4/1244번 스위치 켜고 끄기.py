# 1244번 스위치 켜고 끄기 : https://www.acmicpc.net/problem/1244

def switch(a):  # 0을 1로, 1을 0으로 바꾸는 함수
    if a == 0:
        a = 1
    elif a == 1:
        a = 0
    return a


def male(num, n_stat):  # 남학생일 경우 스위치 변화
    for i in range(num-1, len(n_stat), num):
        n_stat[i] = switch(n_stat[i])
    return n_stat


def female(num, n_stat):  # 여학생일 경우 스위치 변화
    cnt = 1
    while True:
        if num - 1 - cnt < 0 or num - 1 + cnt > len(n_stat) - 1:
            break
        if n_stat[num-1-cnt] == n_stat[num-1+cnt]:
            n_stat[num-1-cnt] = switch(n_stat[num-1-cnt])
            n_stat[num-1+cnt] = switch(n_stat[num-1+cnt])
            cnt += 1
            continue
        else:
            break
    n_stat[num - 1] = switch(n_stat[num - 1])  # 일단 입력받은 순번의 숫자는 무조건 바뀜
    return n_stat


n = int(input())  # 스위치의 갯수, 100이하의 양의 정수
n_stat = list(map(int, input().split()))  # n_stat 배열에 스위치의 상태 입력
student = int(input())  # 학생의 숫자

while student != 0:
    gender, num = map(int, input().split())  # 학생의 성별과 부여받은 번호
    if gender == 1:
        male(num, n_stat)
    if gender == 2:
        female(num, n_stat)
    student -= 1

for i in range(1, len(n_stat)+1):
    print(n_stat[i-1], end=' ')
    if i % 20 == 0:
        print()
