# 9498번 시험 성적 : https://www.acmicpc.net/problem/9498

n = int(input())

if n>=90:
    print("A")
elif n>=80:
    print("B")
elif n>=70:
    print("C")
elif n>=60:
    print("D")
else:
    print("F")