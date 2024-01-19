#1655 가운데를 말해요
#시간제한 때매 입력도 stdin 사용
#중간값 구할때 그냥 정렬 사용해도 시간문제->우선순위 큐 사용

import sys
import heapq

n=int(sys.stdin.readline())     #입력횟수

leftHeap=[]     
rightHeap=[]

for i in range(n):

    num=int(sys.stdin.readline())   #입력할 수

    if len(leftHeap)==len(rightHeap):   #왼쪽 오른쪽 힙의 개수가 같으면 왼쪽에 넣기
        heapq.heappush(leftHeap,-num)    #-는 minHeap에서 최대를 가져와야하므로

    else:
        heapq.heappush(rightHeap,num)   #오른쪽이 더 많을테니까 오른쪽에서 뽑기

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue=heapq.heappop(leftHeap)
        rightValue=heapq.heappop(rightHeap)
        
        heapq.heappush(leftHeap,-rightValue)    #여기서 - 붙어야돼!!!
        heapq.heappush(rightHeap,leftValue)

    print(-leftHeap[0])
    