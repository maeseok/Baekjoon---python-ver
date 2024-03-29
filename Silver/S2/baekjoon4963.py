from collections import deque
import sys
input=sys.stdin.readline
def bfs(graph,x,y):
    dx=[-1,1,0,0,1,1,-1,-1]
    dy=[0,0,-1,1,-1,1,-1,1]
    graph[x][y]=0
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=0
    return 
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    graph =[]
    for i in range(h):
        graph.append(list(map(int,input().split())))
    cnt=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(graph,i,j)
                cnt+=1
    print(cnt)
                