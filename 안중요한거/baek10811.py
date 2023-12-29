# N=5 M=4


# 1 2 3 4 5

# 1 2 :
# 2 1 3 4 5
# 0 1 2 3 4
# 3 4:
# 2 1 4 3 5

# 1 4:
# 3 4 1 2 5

# 2 2:
# 3 4 1 2 5

# N,M 입력받기

# N만큼 배열 생성

# a,b를 입력받아->배열내에서 순서를 바꿈(M 만큼)





#정석대로 풀기
N, M = map(int, input().split())

li=[i for i in range(1,N+1)]           #자동으로 1 2 3 4 5 배열에 넣기 , 리스트 컴프리헨션

for _ in range(M):          #M번 바꾸기
    a,b=map(int,input().split())

    while a<b:
        temp=li[a-1]
        li[a-1]=li[b-1]
        li[b-1]=temp

        a+=1
        b-=1

for i in range(N):
    print(li[i], end=' ')





#간단하게 reverse 함수로 구현
# N, M = map(int, input().split())

# li=[i for i in range(1,N+1)]           #자동으로 1 2 3 4 5 배열에 넣기

# for _ in range(M):          #M번 바꾸기
#     a,b=map(int,input().split())
#     temp=li[a-1:b]
#     temp.reverse()
#     li[a-1:b]=temp


# for i in range(N):
#     print(li[i], end=' ')
