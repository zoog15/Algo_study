# 카드 게임 : https://www.acmicpc.net/problem/5522
g_sum = 0

for i in range(0,5):
    n = int(input())
    if (n >= 0) and (n <= 100):
        g_sum += n
    else:
        break;

print(g_sum)