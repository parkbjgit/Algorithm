import sys
input=sys.stdin.readline
INF=int(1e9)    #무한을 의미 10억

def bf(start):
    #시작노드에 대해서 초기화
    dist[start]=0
    #전체 n번의 반복,         이중for문 사용
    for i in range(n):
        #매 반복마다 간선확인
        for j in range(m):
            cur=edges[j][0]
            next_node=edges[j][1]
            cost=edges[j][2]
            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur]+cost:
                dist[next_node]=dist[cur]+cost
                #n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i==n-1:
                    return True
    return False

#노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
#모든 간선에 대한 정보를 담은 리스트 만들기
edges = []
#최단거리 테이블을 모두 무한으로 초기화
dist= [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c=map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c(가중치)라는 의미
    edges.append((a,b,c))

negative_cycle=bf(1)    #1번 시작노드

if negative_cycle:
    print('-1')

else:
    #1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리 출력
    for i in range(2, n+1):
        #도달할 수 없는 경우, -1 출력
        if dist[i]==INF:
            print("-1")
        #도달할 수 있는 경우 dist[i] 출력
        else:
            print(dist[i])