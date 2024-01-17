import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []      # 빈 리스트를 힙으로 활용
    result = []  # 정렬된 결과를 담을 리스트

    # iterable에서 값을 하나씩 가져와서 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에서 값을 하나씩 꺼내어 결과 리스트에 추가
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

n = int(input())  # 입력 받을 숫자의 개수
arr = []          # 입력 받은 숫자를 담을 리스트

# 숫자를 입력 받아 리스트에 추가
for i in range(n):
    arr.append(int(input()))

# heapsort 함수를 이용해 정렬된 결과를 얻음
res = heapsort(arr)

# 정렬된 결과를 출력
for i in range(n):
    print(res[i])
