#떡 자르기
n,m= map(int, input().split())  #n은 떡의 개수 m은 요청 떡의 길이

array=list(map(int,input().split()))

start=0
end=max(array)
result=0

while (start<=end):
    total=0
    mid=(start+end)//2
    for x in array:
        total=total+(x-mid)

    if total<m:
        end=mid-1
    else:
        result=mid       #최대한 덜 잘랐을 때가 정답이므로, 한번 기록
        start=mid+1

print(result)


#정렬된 배열에서 특정 수의 개수 구하기->log(n)안에, 이진탐색 두번
from bisect import bisect_left, bisect_right

n,m= map(int, input().split())

array=list(map(int,input().split()))

a=bisect_left(array,m) 
b=bisect_right(array,m)

if (b-a)==0:
    print(-1)
else:
    print(b-a)