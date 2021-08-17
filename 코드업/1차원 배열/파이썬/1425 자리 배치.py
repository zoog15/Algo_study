a, b = map(int, input().split())  # a : 총 학생 수 , b : 한줄에 앉힐 수
arr = list(map(int, input().split()))

arr.sort()
cnt = 0

for i in range(a):
    print(arr[i], end=' ')
    cnt += 1
    if cnt % b == 0:
        print()