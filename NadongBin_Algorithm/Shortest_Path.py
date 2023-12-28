#https://velog.io/@tks7205/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python
#간단 설명 링크(아래 코드와 다름)-------다익스트라 알고리즘
import sys
input=sys.stdin.readline
INF=int(1e9)  #무한을 의미 10억

n,m= map(int,input().split())   #노드개수,간선개수
start=int(input())      #시작 노드 번호
graph=[[] for i in range(n+1)]      #노드에 연결되어있는 리스트, 노드는 0이 없기 때문에 n+1까지
visited=[False]*(n+1)           #방문여부 체크리스트    
distance=[INF]*(n+1)            #최단 거리 테이블 무한으로 초기화

for _ in range(m):              #간선정보 입력
    a,b,c=map(int,input().split())      
    graph[a].append((b,c))             #a에서 b로 이동비용이 c

def get_smallest_node():            #방문안한거에서 가장 최단거리가 짧은 노드의 번호반환
    min_value=INF
    index=0                     #가장 최단 거리 짧은 노드(index)
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):    #시작노드에 대해 초기화
    distance[start]=0
    visited[start]=True

    for j in graph[start]:
        distance[j[0]]=j[1]

    for i in range(n-1):    #시작노드를 제외한 전체 n-1개의 노드에 대해 반복
        now=get_smallest_node()     #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        visited[now]=True

        for j in graph[now]:    #현재 노드와 연결된 다른 노드를 확인
            cost=distance[now]+j[1] 
            if cost<distance[j[0]]: #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은경우
                distance[j[0]]=cost

dijkstra(start) 

for i in range(1,n+1):
    if distance[i]==INF:    #도달할수 없는 경우
        print("infinity")
    else:
        print(distance[i])


#내림차순 힙 정렬(라이브러리)-기본이 오름차순이라 -이용
import heapq

def heapsort(iterable):
    h=[]
    result=[]

    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#우선순위큐-다익스트라
#https://techblog-history-younghunjo1.tistory.com/248
import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)  #무한을 의미 10억

n,m= map(int,input().split())   #노드개수,간선개수
start=int(input())      #시작 노드 번호
graph=[[] for i in range(n+1)]      #노드에 연결되어있는 리스트, 노드는 0이 없기 때문에 n+1까지
visited=[False]*(n+1)           #방문여부 체크리스트    
distance=[INF]*(n+1)            #최단 거리 테이블 무한으로 초기화

for _ in range(m):              #간선정보 입력
    a,b,c=map(int,input().split())      
    graph[a].append((b,c))             #a에서 b로 이동비용이 c


def dijkstra(start):            
    q=[]
    heapq.heappush(q,(0,start)) #시작 노드로 가기위한 최단 거리는 0으로 설정하여 큐에 삽입
    distance[start]=0
    while q:    #큐가 비어있지않다면
        dist,now=heapq.heappop(q)   #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

        if distance[now]<dist:  #현재 노드가 이미 처리된 적이 있으면 무시,*더 크다면 이미 처리가 된 것으로 간주 가능
            continue

        for i in graph[now]:    #현재 노드와 연결된 다른 인접 노드들을 확인
            cost=dist+i[1]      #i[1]은 거리값

            if cost<distance[i[0]]: #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(start) 

for i in range(1,n+1):
    if distance[i]==INF:    #도달할수 없는 경우
        print("infinity")
    else:
        print(distance[i])