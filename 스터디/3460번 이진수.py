T = int(input()) # 테스트 케이스 갯수
a=[]
idx = 0

for i in range(1,T+1) : # T번 반복
    n = int(input()) # 양의 정수 입력
    while n != 0 : # a리스트 안에 이진수 역순으로 저장됨
        if n%2 == 1 :
            a.append(1) # 나머지가 1이면 a에 1추가
        else :
            a.append(0) # 나머지가 0이면 a에 0 추가
        n = n//2
    for j in a :
        if j == 1 :
            print(idx,end=" ")
        idx+=1
    print()
    a.clear()
    idx = 0




