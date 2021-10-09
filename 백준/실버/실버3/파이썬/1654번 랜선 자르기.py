import sys

# k: 가지고있는 랜선 개수, n: 필요한 랜선 개수
k, n = map(int, sys.stdin.readline().split())
lines = []

# 랜선의 길이들 입력
for i in range(k):
    lines.append(int(sys.stdin.readline()))

start = 1
end = max(lines)

result = 0
while start <= end:
    mid = (start + end) // 2
    line = 0
    # print(start, end, mid)
    # mid에 따라 만들어진 랜선 개수
    for i in lines:
        line += i // mid

    if line < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

