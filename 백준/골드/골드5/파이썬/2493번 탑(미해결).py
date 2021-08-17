#2493번 탑 : https://www.acmicpc.net/problem/2493

# 5
# 6 9 5 7 4
n = int(input())  # 탑의 수
a = list(map(int, input().split()))  # 탑의 높이를 입력하는 배열
answer = [] # 0 0 2 2 4

# 접근3 : ㅠㅠ




# 접근2 : pop을 쓰면서 해보기 -> 시간초과
# for i in range(0, n):
#     last = a.pop()
#     for j in range(0, len(a)):
#         if a[len(a)-j-1] > last:
#             answer.append(a.index(a[len(a)-j-1])+1)
#             break
#         if j == len(a)-1:
#             answer.append(0)
#
# answer.append(0)
# answer.reverse()
# print(answer)

# 접근1 : 그냥 2중for문 - 시간초과
# answer = []
# answer.append(0)  # 첫값은 무조건 0임
#
# for i in range(1, n):
#     for j in range(i, -1, -1):
#         # print(a[i], a[j])
#         if a[j] > a[i]:
#             answer.append(a.index(a[j])+1)
#             break
#         if j==0:
#             answer.append(0)
#
# print(answer)
