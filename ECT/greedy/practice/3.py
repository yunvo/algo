''' 
이코테
greedy #3 숫자 카드 게임
'''

n, m = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(n)]

max = 0
for i in range(n):
  # card[i].sort()
  if (max < min(card[i])):
    max = min(card[i])

print(max)


# 입력과 동시에 검증
n, m = map(int, input().split())

ans = 0
for i in range(n):
  card = list(map(int, input().split()))
  ans = max(min(card), ans)
  
print (ans)

