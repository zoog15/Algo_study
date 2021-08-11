# 16170번 오늘의 날짜는? : https://www.acmicpc.net/problem/16170

import datetime

# datetime.datetime.now() -> 현재 시간을 YYYY-MM-DD hh:mm:ss 로 받아옴
# datetime.timedelta(hours= int) -> 시차를 계산할때 쓰는 방법. 영국(세계)표준시(UTC+0)는  한국표준시(UTC+9) 보다 9시간 느림 
time = datetime.datetime.now() + datetime.timedelta(hours=-9)

print(time.year)
print(time.month)
print(time.day)