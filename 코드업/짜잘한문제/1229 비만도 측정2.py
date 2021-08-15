a, b = map(float, input().split())

if a < 150:
    aw = a - 100
elif a<160:
    aw = ((a-150)/2) + 50
else:
    aw = (a-100)*0.9

ws = (b-aw)*100/aw

if ws <= 10:
    print("정상")
elif ws <= 20:
    print("과체중")
else:
    print("비만")
