''' 
이코테
dynamic programming #5 효율적인 화폐 구성
'''

'''
점화식


d[i] = min(d[i-arr[0..n-1]]) + 1

'''

n, m = map(int,input().split())
coin = []

for _ in range(n):
  coin.append(int(input()))

d = [-1] * 10001
# 동전과 같은 금액은 1번만에 도달 가능
for i in range(0, n):
  d[coin[i]] = 1

d[0] = 0

for i in range(0, m+1):
  for j in range(0, n):
    # i - coin[j]원이 가능하면
    if (d[i-coin[j]] != -1):
      # 이미 동전 조합이 가능하면
      if (d[i] != -1):
        # 그 조합 값과 지금의 값을 비교
        d[i] = min(d[i], d[i-coin[j]] + 1)
      # 동전 조합이 없었으면 반영
      else:
        d[i] = d[i-coin[j]] + 1
      
print(d[m])

'''
동전 갯수가 최대가 되는 경우는
10000원을 1원짜리로 가지는 경우이므로
최대값은 10000이다.
'''

n, m = map(int, input().split())
array = []
for _ in range(n):
  array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0

# 각 동전 별
for i in range(n):
  # 해당 동전보다 낮은 금액은 찾아볼 필요가 없다.
  for j in range(array[i], m+1):
    # 이 조건문은 생략 가능
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j-array[i]]+1)

if d[m] != 10001:
  print(d[m])
else:
  print(-1)
