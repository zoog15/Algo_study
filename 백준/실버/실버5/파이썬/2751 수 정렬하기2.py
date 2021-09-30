# 2751번 수 정렬하기2 : https://www.acmicpc.net/problem/2751
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

print(*arr,sep='\n')

