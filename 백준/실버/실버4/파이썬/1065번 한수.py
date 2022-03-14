# https://www.acmicpc.net/problem/1065

def HanSoo(num):
    # 한,두자리숫 자이면 무조건 한수
    if 0 <= num // 10 <= 9:
        return True
    else:
        baek = num // 100
        sip = (num//10)% 10
        ill = num%10
        if (baek-sip) ==  (sip - ill):
            return True
        else:
            return False



# 숫자 입력
n = int(input())
count = 0

for i in range(1, n+1):
    if HanSoo(i):
        count += 1

print(count)