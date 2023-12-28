#DFS ->stack
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph=[
    [],
    [2,3,8],
    ...
]

visited = [False]*9

dfs(graph,1, visited)


#BFS ->queue#
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v= queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            queue.append(i)
            visited[i]= True

graph=[
    [],
    [2,3,8],
    ...
]
visited = [False]*9
bfs(graph,1, visited)


#dfs 를 이용해서 음료수 얼려먹기(얼음 총 몇개?)#
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    
    return False

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)


#BFS를 사용한 미로탈출
def bfs(x,y):
    queue =  deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:  #맵 밖으로 나가는 경우
                continue

            if graph[nx][ny] == 0:      #괴물 만나는 곳
                continue

            if graph[nx][ny] ==1:        #갈 수 있는 길
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]      #마지막 노드


from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))