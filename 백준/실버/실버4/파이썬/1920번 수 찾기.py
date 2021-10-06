n = int(input())  # n개의 정수
number = list(map(int, input().split()))  # 저장된 숫자
m = int(input())  # 비교할 숫자 개수
compare = list(map(int, input().split()))  # 비교할 숫자들
number.sort()


def binary_search(number, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if number[mid] == target:
            return 1
        elif number[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in range(m):
    target = compare[i]
    print(binary_search(number, target, 0, len(number)-1))