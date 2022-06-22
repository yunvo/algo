''' 
이코테
sorting #3 성적이 낮은 순서로 학생 출력하기
'''

n = int(input())

student = []

for _ in range(n):
  name, grade = input().split()
  student.append([name, int(grade)])

student.sort(key=lambda data: data[1])

for s in student:
  print(s[0], end=' ')


# 다른 방법 (튜플 사용)
n = int(input())
array = []

for _ in range(n):
  data = input().split()
  array.append((data[0], int(data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
  print(student[0], end=' ')
