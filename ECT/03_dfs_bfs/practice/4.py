'''
이코테
DFS/BFS #4 미로 탈출
'''
from collections import deque

q = deque()
n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int,input())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

ans = 0

def bfs(root):
  q.append(root)
  
  while q:
    cur = q.popleft()
    # 종료조건
    if cur[0] == m-1 and cur[1] == n-1:
      print(cur[2])
      break
      
    for i in range(4):
      nx = cur[0] + dx[i]
      ny = cur[1] + dy[i]
      depth = cur[2] + 1
      if nx >= 0 and nx < m and ny >= 0 and ny < n:
        if graph[ny][nx] == 1:
          q.append((nx,ny,depth))

bfs((0,0,1))

# queue에서 값 뽑아낼 때 tuple로 뽑아낼 필요 없이 x, y로 뽑아내면 됨
'''
x, y, depth = q.popleft()
'''
