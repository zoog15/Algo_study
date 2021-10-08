import sys


def isVPS(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if not stack or stack[-1] == ')':
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False


T = int(sys.stdin.readline())  # 테스트 케이스 수

for i in range(T):
    s = list(sys.stdin.readline().strip())
    if isVPS(s):
        print("YES")
    else:
        print("NO")