# 1259번 팰린드롬수 : https://www.acmicpc.net/problem/1259
def Ispalindrome(n):
    cen = len(n) // 2  # 배열의 중간 인덱스
    if len(n) % 2 == 1:  # 길이가 홀수
        for i in range(cen):
            # print(n[cen - i-1], n[cen + i+1])
            if n[cen-i-1] != n[cen+i+1]:
                return False
        return True
    else:
        for i in range(cen):
            # print(n[cen - i-1], n[cen + i])
            if n[cen-1-i] != n[cen+i]:
                return False
        return True


while True:
    n = input()  # 검사하기 편하게 문자열로 입력받기기
    if n == '0':
        break
    if Ispalindrome(n):
        print("yes")
    else:
        print("no")
