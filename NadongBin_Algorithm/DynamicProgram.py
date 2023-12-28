# #fibinacci#
# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     return fibo(x-1)+fibo(x-2)

# print(fibo(4))


# #topdown#
# d=[0]*100

# def fibo(x):
#     if x==1 or x==2:
#         return 1
    
#     if d[x]!=0:
#         return d[x]
    
#     d[x]=fibo(x-1)+fibo(x-2)
#     return d[x]

# print(fibo(99))


# #bottomup#
# d=[0]*100

# d[1]=1
# d[2]=1
# n=99

# for i in range(3,n+1):
#     d[i]=d[i-1]+d[i-2]

# print(d[n])


# #개미 전사#
# n=int(input())
# array=list(map(int,input().split()))

# d=[0]*n

# d[0]=array[0]       #초기값
# d[1]=max(array[0],array[1])  #i=1일때도 둘중에 더 큰값

# for i in range(2,n):

#     d[i]=max(d[i-1],d[i-2]+array[i])

# print(d[n-1])


# #1로 만들기-2,3,5 로 나누거나 1을 빼는 연산으로 연산횟수의 최소를 구함??????
# #전에 했던 단순한 그리디 해법과는 다름- 1을 빼거나 2,3으로 나누는게 나을수도
# x=int(input())

# d=[0]*30001

# for i in range(2,x+1):
#     d[i]=d[i-1]+1   #현재의 수에서 1을 빼는 경우

#     if i%2==0:      #현재의 수가 2로 나누어 떨어질 경우
#         d[i]=min*(d[i],d[i//2]+1)
#     if i%3==0:
#         d[i]=min*(d[i],d[i//3]+1)
#     if i%5==0:
#         d[i]=min*(d[i],d[i//5]+1)
# print(d[x])



# #효율적인 화폐구성
# n,m=map(int,input().split())    #n개의 화폐단위, m은 금액

# array=[]
# for i in range(n):
#     array.append(int(input))        #화폐 입력

# d=[10001]*(m+1)

# d[0]=0
# for i in range(n):
#     for j in range(array[i], m+1):  
#         if d[j-array[i]]!=10001:       #(i-k)원을 만드는 방법이 존재
#             d[j]=min(d[j], d[j-array[i]]+1) #동전개수 +1 하기

# if d[m]==10001:
#     print(-1)
# else:
#     print(d[m])


#금광캐기
# 	j 0123   m
# i
# 0
# 1
# 2
# n
for tc in range(int(input())):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))

    dp=[]
    index=0

    for i in range(n):  #배열에 넣기
        dp.append(array[index:index+m])
        index+=m
    

    for j in range(1,m):        #i->y j->x
        for i in range(n):
            #왼쪽위에서 옴
            if i==0: left_up=0
            else: left_up=dp[i-1][j-1]
            #왼쪽아래에서
            if i==n-1: left_down=0
            else: left_down=dp[i+1][j-1]
            #왼쪽에서
            left=dp[i][j-1]
            dp[i][j]=dp[i][j]+max(left_up,left_down,left)
    result=0
for i in range(n):
    result=max(result,dp[i][m-1])
print(result)



#병사배치문제 전투력 높은애가 앞으로(LIS 알고리즘)
n=int(input())
array=list(map(int,input().split()))

array.reverse() #순서를 뒤집어 '최장 증가 부분수열'문제로 변환

dp=[1]*n


for i in range(1,n):        #가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
