a, b = map(float, input().split())

aw = (a-100)*0.9  # 표준 몸무게
ws = (b-aw)*100/aw

if ws <= 10:
    print("정상")
elif ws <= 20:
    print("과체중")
else:
    print("비만")