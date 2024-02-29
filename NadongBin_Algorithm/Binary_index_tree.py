#binary index tree
import sys
input=sys.stdin.readline


#데이터의 개수, 업데이트 횟수, 구간합을 계산할 횟수
n,m,k=map(int,input().split())

#데이터의 최대갯수 배열 arr, tree 
arr=[0]*(n+1)
tree=[0]*(n+1)

#1~end까지 모두 더하기      xxxxxx
def prefix_sum(i):
    result=0
    while i>0:
        result+=tree[i]
        i-=(i&-i)       ###비트계산->가장 오른쪽에 있는 '1'비트 제거!!
    return result

#i번째수를 diff만큼 더하는 함수
def update(i,diff):
    while i<=n:
        tree[i]+=diff
        i+=(i&-i)



#start부터 end까지의 구간합 뺀거
def interval_sum(start,end): 
    return prefix_sum(end)-prefix_sum(start-1)        #이때 start-1까지


for i in range(1,n+1):      #
    x=int(input())
    arr[i]=x
    update(i,x)


for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:    #update 연산인경우
        update(b,c-arr[b])
        arr[b]=c
    else:   #구간합 연산인 경우
        print(interval_sum(b,c))
