''' 
이코테
dynamic programming #4 바닥 공사
'''

'''
점화식

DP는 점화식만 잘 세우면 된다.
'잘' 세우는게 중요하다.

# 1x2, 2x1 2개, 2x2 1개
d[i] = d[i-1] + d[i-2] + d[i-2]
'''

n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
  d[i] = d[i-1] + 2 * d[i-2]
  
print(d[n])
