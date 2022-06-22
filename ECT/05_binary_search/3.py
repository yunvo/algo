''' 
이코테
binary searching #3 떡볶이 떡 만들기
'''
# parametric search는 반복문으로 구현하는게 좋음
import sys

def binary_search(array,target,start,end):
  ans = 0
  while start <= end:
    mid = (start + end) // 2
    # 떡을 mid에서 자른다고 했을 때
    # 잘린 나머지 떡 (mid+1부터 끝까지)의 길이의 합
    x = sum(array[mid+1:]) - (array[mid] * (end - mid))
    # 남은 떡 길이가 길면 덜 잘라야 함
    if x >= target:
      # '적어도' H 만큼이 정답이므로 현재 위치 기록
      ans = mid
      start = mid+1
    # 남은 떡 길이가 짧을때는 더 잘라야 함
    else:
      end = mid-1

  return ans
    

n, h = map(int,input().split())

array = list(map(int,sys.stdin.readline().split()))
array.sort()

print(array[binary_search(array,h,0,n-1)])

