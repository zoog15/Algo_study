a, b = map(int, input().split())

if a%2 == 0:
    s1 = "짝수"
else:
    s1 = "홀수"

if b%2 == 0:
    s2 = "짝수"
else:
    s2 = "홀수"

if s1 == "홀수" and s2 == "홀수":
    print("홀수+홀수=짝수")
elif s1 == "홀수" and s2 == "짝수":
    print("홀수+짝수=홀수")
elif s1 == "짝수" and s2 == "홀수":
    print("짝수+홀수=홀수")
else:
    print("짝수+짝수=짝수")