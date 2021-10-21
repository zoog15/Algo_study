n = int(input())  # 약수의 개수
arr = list(map(int, input().split()))  # 진짜 약수

arr.sort()

answer = max(arr) * min(arr)

print(answer)