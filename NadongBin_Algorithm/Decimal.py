#소수찾기-에라토스테네스의 체#
import math
n=1000  #1~1000까지

array=[True for i in range(n+1)]        #1~1000까지 배열 True로 초기화

#2부터 sqrt(n)까지 돌면서 배수들 제거
#만약 i번재가 true 라면 j 초기화해서 배수들을 False로 바꿈(while ixj사용)
for i in range(2,int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j<=n:
            array[i*j]=False
            j+=1    #이거 빼먹음####

#array중에 true인 것만 리스트 출력
for i in range(2,n+1):  #1은 당연히 소수가 아니고, n=1000이니까 n+1이지
    if array[i]:
        print(i, end=' ')



#투포인트-특정 합을 만족하는 연속된 부분배열
#부분합 입력받기
n=5
m=5     #부분합

array=[1,2,3,2,5]

interval_sum=0
count=0
end=0


#1~리스트 길이만큼 반복문
for start in range(1,n+1):
#if 배열의 부분합<특정 부분합 이라면 end+1, 임시 sum+array[end] 
    while interval_sum<m and end<n:        #여기서 while문 사용####
        interval_sum+=array[end]
        end+=1
    if interval_sum==m:         
        count+=1            
    #여기서 빼먹은거###
    interval_sum-=array[start]

print(count)
 


#구간합 빠르게 계산하기
n=5
array=[10,20,30,40,50]

sum_value=0
prefix_sum=[0]

for i in array:
    sum_value+=i
    prefix_sum.append(sum_value)      #i를 추가할게 아니라 sum_value를 넣어야지###

left=3
right=4

print(prefix_sum[right]-prefix_sum[left-1])  #3~4까지의 합###