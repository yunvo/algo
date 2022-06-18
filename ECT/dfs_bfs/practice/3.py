'''
이코테
DFS/BFS #3 음료수 얼려 먹기
'''

n, m = map(int, input().split())
tray = [list(map(int,input())) for _ in range(n)]
v = [[False for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0

def dfs(x, y, adj, v):
  if (v[y][x] == True or adj[y][x] == 1):
    return

  # visit check
  v[y][x] = True

  # adj node search
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (nx < m and nx >= 0 and ny < n and ny >= 0):
      dfs(nx,ny,adj,v)


for i in range(n):
  for j in range(m):
    if tray[i][j] == 0 and v[i][j] == False:
      ans += 1
      dfs(j,i,tray,v)

print(ans)

# 방문 배열을 따로 두지 않아도 됨
n, m = map(int, input().split())

# 2차원 입력 받아오기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 세로가 x, 가로가 y
def dfs(x, y):
  # 종료 조건: 범위 벗어날 경우
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  # 수행 조건: 노드 방문하지 않았을 경우
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  
  return False

ans = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      ans += 1

print(ans)
