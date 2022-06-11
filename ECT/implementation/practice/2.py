'''
이코테
implementation #2 왕실의 나이트
'''

knight = input()
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
ans = 8

for i in range(8):
  if ord(knight[0]) + dx[i] > ord('h') or ord(knight[0]) + dx[i] < ord('a'):
    ans -= 1
  elif ord(knight[1]) + dy[i] > ord('8') or ord(knight[1]) + dy[i] < ord('1'):
    ans -= 1

print(ans)


# steps list로 풀기
knight = input()
row = int(knight[1])
column = int(ord(knight[0])) - int(ord('a')) + 1

steps = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]

ans = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    ans += 1

print(ans)
