# 요일을 저장해놓는 배열
WEEK = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# 월과 일을 입력받기
mon, day = map(int, input().split())

# 각 월에 대한 일 수
num_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 1년은 365일
year = 365

for i in range(1, mon):
    year -= num_day[i]


now_day = (365 - year) + day - 1

now_day %= 7

print(WEEK[now_day])