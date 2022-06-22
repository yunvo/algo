''' 
이코테
binary searching #2 부품 찾기
'''

# 이진 탐색 사용하는 방법
# 탐색 + 정렬 시간 소요
# O(MlogN) + O(NlogN) = O((M+N)logN)

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if target == array[mid]:
      return mid
    elif target > array[mid]:
      start = mid+1
    else:
      end = mid-1
  return None

n = int(input())
array = list(map(int,input().split()))
# 이진 탐색을 위해 정렬
array.sort()

m = int(input())
offer = list(map(int,input().split()))

for i in offer:
  ans = 'yes' if binary_search(i, 0, n-1) != None else 'no'
  print(ans, end=' ')


# radix sort 사용하는 방법
n = int(input())
array = [0] * 1000001

for i in input().split():
  array[int(i)] += 1

m = int(input())
x = list(map(int,input().split()))

for i in x:
  if array[i] != 0:
    print('yes', end=' ')
  else:
    print('no', end=' ')

# set 자료형 사용하는 방법
n = int(input())
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
  # set 안에 있는지 확인
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
