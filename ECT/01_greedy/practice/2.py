''' 
이코테
greedy #2 큰 수의 법칙
'''
ans = 0
n, m, k = map(int, input().split())
l = list(map(int,input().split()))
l.sort()
for i in range(m):
  if i%k == 0 and i != 0:
    ans += l[-2]
  else:
    ans += l[-1]

print(ans)


'''
더 빠른 풀이
'''
n,m,k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

first = l[-1]
second = l[-2]

# fffs 갯수
count = int(m/(k+1))*k
# 나머지 f
count += m % (k+1)

ans = 0
ans += count * first
ans += (m-count) * second

print(ans)
