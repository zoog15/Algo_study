import sys


n = int(sys.stdin.readline())  # 설탕의 무게

count = 0  # 봉투의 개수

while n >= 0:
    if n % 5 == 0:
        mok = n // 5
        count += mok
        n -= 5 * mok
        break
    n -= 3
    count += 1

if n == 0:
    print(count)
else:
    print(-1)


