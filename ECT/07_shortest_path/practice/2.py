''' 
이코테
shortest path #2 미래 도시
'''
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  # no direct
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
  graph[i][i] = 0

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

ans = graph[1][k] + graph[k][x]

# 0 + INF인 경우도 고려해야 함
if ans >= INF:
  ans = -1

print(ans)
