#선택 정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(0, len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[min_index],array[i]=array[i],array[min_index] #swap 들여쓰기 하나로 결과가 다르다 조심

print(array)    

#삽입 정렬-살짝 더 빠름
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):           #index=1 부터 왼쪽이랑 바꿈
    for j in range(i,0,-1):
        if array[j] < array[j-1]:           #한칸씩 왼쪽으로 이동
            array[j],array[j-1]=array[j-1],array[j]        
        else:           #나머지는 비교할 필요가 없음
            break

print(array)


#퀵 정렬1
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot=start 
    left=start+1 
    right=end 
    while(left<=right): 
        while(left <= end and array[pivot]<=array[left]):   #피벗보다 큰 값을 찾을 때까지 
            left+=1 
        while(right > start and array[pivot]>=array[right]):    #피벗보다 작은 값을 찾을 때까지
            right-=1 

        if left>right:      #엇갈렸다면 작은값(right)과 피벗과 교체
            array[pivot], array[right]= array[right],array[pivot]

        else:               #안엇갈리면 left,right 교체
            array[left], array[right]= array[right],array[left]

    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)


#퀵 정렬2
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


#퀵 정렬 간단 버전
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:]

    left_side=[x for x in tail if x <= pivot]
    right_side=[x for x in tail if x > pivot]

    return quick_sort(left_side)+ [pivot] + quick_sort(s=right_side)

print(quick_sort(array))


#계수 정렬-배열의 최대,최소를 확인하고 그 범위에서 해당 숫자의 개수를 기록
#0, 999999 있으면 그 사이에 너무 많은 공간복잡도 필요
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')



#배열의 최대 합 만들기
n,k = map(int ,input().split())

a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break

print(sum(a))