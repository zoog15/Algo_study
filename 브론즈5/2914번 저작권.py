a, avg = map(int, input().split())  # 수록된 곡의 갯수와 올림한 평균값

result = (a*(avg-1)) + 1

print(result)
