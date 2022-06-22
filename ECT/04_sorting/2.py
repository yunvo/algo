''' 
이코테
sorting #2 위에서 아래로
'''

n = int(input())
ans = []

for _ in range(n):
  ans.append(int(input()))

ans.sort(reverse=True)

for i in ans:
  print(i, end=' ')
