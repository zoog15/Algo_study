a,b = map(int,input().split()) # a = 1m^2당 사람의 수, b = 파티 열린곳의 넓이

news = list(map(int,input().split())) # 기사별 참가자의 수 5개 입력

people = a*b # 파티에 참석한 사람 수

for i in news :
    print(i-people,end=" ")
