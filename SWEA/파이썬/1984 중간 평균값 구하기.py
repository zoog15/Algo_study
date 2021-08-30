T = int(input())  # 테스트 케이스

for tc in range(T):
    a = list(map(int, input().split()))
    a.sort()
    a[0] = 0
    a[9] = 0
    sum_a =sum(a)

    print(f'#{tc+1} {format(sum_a/8, ".0f")}')