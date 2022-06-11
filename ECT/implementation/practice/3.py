'''
이코테
implementation #3 게임개발
'''

n, m = map(int,input().split())
x, y, d = map(int,input().split())
l = [list(map(int, input().split())) for _ in range(m)]
v = [[0 for _ in range(n)] for _ in range(m)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = 1


while True:
  # print(l)
  # print(v)
  if v[x][y] == 0:
    v[x][y] = 1
  else:
    break
    
  for i in range(4):
    # 방향 설정
    d = (d+i)%4
    nx = x + dx[d]
    ny = y + dy[d]
    # print(d, nx, ny)
    if nx < m and nx >= 0 and ny < n and ny >= 0:
      # 갈 수 있으면
      if l[nx][ny] != 1 and v[nx][ny] != 1:
        x = nx
        y = ny
        ans += 1
        break

print(ans)

# 구현은 조건만 보고 조건에 부합하게만 구현하면 됨
