''' 
이코테
greedy #4 1이 될 때까지
'''

n, k = map(int, input().split())
ans = 0

while n > 1:
  if n%k ==0:
    n /= k
  else:
    n -= 1

  ans += 1

print(ans)

# 1씩 빼는 과정 줄이기

n, k = map(int, input().split())
ans = 0

while True:
  target = (n // k) * k
  ans += (n - target)

  if (n < k):
    break

  ans += 1
  n /= k

result += (n-1)

print(ans)
