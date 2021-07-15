N = int(input())

a = list(map(int,input().split())) # N개만큼 입력해서 리스트에 저장

max = a[0]; min = a[0]

for i in a :
    if i > max :
        max = i
    if min > i :
        min = i

print(min,max)
