#그리디 알고리즘 연습문제들-나동빈-#

#1이 될때까지 문제 ################
N,K=input().split()   
N=int(N)
K=int(K)

cnt=0

while True:
    target=(N//K)*K     #가까운 타겟을 정하면 한 루프안에서 이루어져서 로그
    cnt=cnt+(N-target)  
    N=target

    if N<K:
        break

    cnt+=1
    N//=K

cnt+=(N-1)
print(cnt)







#더하기 곱하기################
data=input()
result =int(data[0])

for i in range(1, len(data)):       #1이라면 곱보단 더하는게 더 큼
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
print(result)






#모험가 길드원 그룹 나누기################
n=int(input())
data = list(map(int,input().split()))
data.sort()     #오름차순 정렬로 해야 낮은 수부터 결성 가능

result=0
count=0     #모험가를 포함 시킬 그룹원 수

for i in data:
    count+=1    #현재 그룹원 수
    if i>=count:    #그룹원의 공포도 i가 그룹원수 
        result+=1   #전체 그룹 +1
        count=0     #현재 그룹원 수 초기화

print(result)   #총 그룹의 수 출력



#모험가 상하좌우 이동################
N=int(input())
plans = input().split()
x,y = 1,1

# u d r l
dx=[0,0,1,-1]
dy=[-1,1,0,0]
move_types=['U','D','R','L']    

for plan in plans:
    for i in range(4):
        if move_types[i]== plan:
            nx=x+dx[i]
            ny=y+dy[i]

    if nx<1 or nx>N or ny<1 or ny>N:    #밖으로 벗어났을 때
        continue

    x,y=nx,ny
print(x,y)


# 0시0분0초~N시59분59초   3이 포함된 시간의 개수세기################
h=int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)





#체스 나이트가 이동할 수 있는 경우의 수############
input_data=input()
row=int(input_data[1])                                   #row가 y좌표
column=int(ord(input_data[0]))-int(ord('a'))+1          #column이 x좌표
result=0
steps=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]

    if next_row<=8 or next_row>=1 or next_column<=8 or next_column>=1:
        result+=1

print(result)