#dfs 연결된 컴퓨터들은 감염, 1번과 연결된 컴퓨터 개수 구하기
n=int(input())
v=int(input())
graph=[[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(v):  
    a,b=map(int,input().split())
    graph[a]+=[b]   
    graph[b]+=[a]

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:  #만약 아직 방문하지 않은 점이라면 다시 dfs 실행
            dfs(nx)

dfs(1)
print(sum(visited)-1)   #방문했다면 visited가 1일 것이므로 다 더하면 연결된 컴퓨터개수



#bfs로 풀기
from collections import deque
n=int(input())
v=int(input())
graph=[[] for i in range(n+1)]
visited=[0]*(n+1)

for i in range(v):  
    a,b=map(int,input().split())
    graph[a]+=[b]   
    graph[b]+=[a]

visited[1]=1
queue=deque([1])
while queue:
    c=queue.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            queue.append(nx)
            visited[nx]=1
print(sum(visited)-1)
