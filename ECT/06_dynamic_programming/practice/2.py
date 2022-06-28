''' 
이코테
dynamic programming #2 1로 만들기
'''

n = int(input())
d = [0]*(n+1)

for i in range(2,n+1):
  val = 30000
  if d[i] == 0:
    if i % 5 == 0:
      val = min(val, d[int(i/5)] + 1)
      #print(i, d[i], i/5, d[int(i/5)])
    if i % 3 == 0:
      val = min(val, d[int(i/3)] + 1)
      #print(i, d[i], i/3, d[int(i/3)])
    if i % 2 == 0:
      val = min(val, d[int(i/2)] + 1)
      #print(i, d[i], i/2, d[int(i/2)])
    
    val = min(val, d[i-1] + 1)
    #print(i, d[i], i-1, d[i-1])
    d[i] = val
  
  #print(i, d[i])

print(d[n])


'''
변수 선언 없이도 문제 해결 가능
'''

n = int(input())
d = [0]*30001

for i in range(2, n+1):
  d[i] = d[i-1] + 1
  if d[i] % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1)
  if d[i] % 3 == 0:
    d[i] = min(d[i], d[i//3] + 1)
  if d[i] % 5 == 0:
    d[i] = min(d[i], d[i//5] + 1)

print(d[n])
