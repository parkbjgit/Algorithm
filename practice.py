# import sys
# from itertools import permutations

# #(1) 순열만들기
# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int, input().split()))
# p = list(permutations(arr, n))

# answer = 0
# for i in p:
#     print(i)
#     s = 0
# # (2) 반복문으로 튜플을 꺼내 각 순열마다 차이의 합(s)을 구하고, 최대값을 answer에 저장한다
#     for j in range(n-1):
#         s += abs(i[j] - i[j+1])
# # 모든 경우 원소들끼리의 차이의 절댓값의 합을 max함수를 이용하여 갱신
#     answer = max(answer, s)

# print(answer)

#import sys
# n,m=map(int,sys.stdin.readline().split())
# lst=list(map(int,sys.stdin.readline().split()))

# start,end=1,max(lst)

# while start <= end:
#     sum=0
#     mid=(start+end) // 2        #중간값설정
    
#     for l in lst:
#         if l > mid:
#             sum+=l-mid

#     if sum<m:
#         end=mid-1
#     else:
#         start=mid+1

# print(end)

# 집개수 5 공유기개수 3
# 공유기의 x좌표들
# 1 2 8 4 9
# 1 2 4 8 9
# o   o    o


#https://my-coding-notes.tistory.com/119
n,c= map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start=1
end=arr[-1]-arr[0]      #제일큰거-제일작은거
result=0

while (start<=end):
    mid=(start+end) //2
    current=arr[0]
    count=1

    for i in range(1,len(arr)):     #집개수만큼
        if arr[i] >= current+mid:   #집이 중간+제일 왼쪽
            count+=1
            current=arr[i]

    if count >= c:
        start=mid+1
        result=mid

    else:
        end=mid+1

print(result)