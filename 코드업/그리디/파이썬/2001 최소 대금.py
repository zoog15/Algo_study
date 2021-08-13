# 그리디 2001 최소대금 : https://codeup.kr/problem.php?id=2001
min_p = 2000  # 파스타 최소금액 저장용
min_s = 2000  # 샐러드 최소금액

for i in range(3):
    p = int(input())
    if p < min_p:
        min_p = p

for i in range(2):
    s = int(input())
    if s < min_s:
        min_s = s

print(format((min_p+min_s)*1.1, ".1f"))