''' 
이코테
dynamic programming #3 개미 전사
'''

'''
점화식
i = max(i+2, i+3) + i
단 0에서 시작하거나 1에서 시작하거나의 두 가지 경우를 고려
max(0,1)
'''

n = int(input())
d = list(map(int, input().split()))

d[n-3] = d[n-1] + d[n-3]
for i in range(n-4,0,-1):
  d[i] = max(d[i+3], d[i+2]) + d[i]

print(max(d[0], d[1]))

'''
1. i 번째 포함
2. i 번째 미포함
의 두 가지 경우의 수의 max 값을 취하면 됨
'''

n = int(input())
food = list(map(int, input().split()))

d = [0] * 100

# 0인 경우는 max(f[0])임
d[0] = f[0]
# 1인 경우도 무조건 max값 취해줘야 함
d[1] = max(f[0], f[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + f[i])

print(d[n-1])
