p,q = map(int,input().split())

a = [] # 약수들을 저장하기위한 리스트
cnt = 0

for i in range(1,p+1) : # 1부터 p까지
    if p%i == 0 : # 나누어 떨어지면
       a.append(i)
       
n = len(a)

if n < q :
    print("0")
else:
    print(a[q-1])
 
