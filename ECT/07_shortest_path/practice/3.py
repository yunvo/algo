''' 
이코테
shortest path #2 전보
'''
import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
  a, b, weight = map(int, input().split())
  # 거리, 노드순으로
  graph[a].append((weight, b))

def dijkstra(start):
  q = []
  
  heapq.heappush(q,(0,start))
  distance[start] = 0
  
  while q:
    dist, cur = heapq.heappop(q)
    if distance[cur] < dist:
      continue

  # 거리 - 노드 순
  for i in graph[cur]:
    cost = dist + i[0]
    if cost < distance[i[1]]:
      distance[i[1]] = cost
      heapq.heappush(q,(cost,i[1]))

dijkstra(c)

cnt = 0
max_distance = 0

for d in distance:
  if d != INF:
    cnt += 1
    max_distance = max(max_distance, d)

print(cnt -1, max_distance)
