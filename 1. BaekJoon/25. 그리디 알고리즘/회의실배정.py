# 회의의 수
n = int(input())

time = []

for i in range(n):
  time.append(list(map(int,input().split())))

# print(time)

# 회의 끝나는 시간 오름차순 정렬
time.sort(key=lambda x:x[1]) # 예외 : [[6, 6], [5, 6], [4, 6], [3, 6], [2, 6]]

# 첫번째 회의 끝나는 시간
x = time[0][1]

# 최대 회의 수 저장 변수
result1 = 1

for i in range(1,n):
  if x <= time[i][0]:
    # print(f"{x} <= {time[i][0]}")
    x = time[i][1]
    result1 +=1

# 회의 시작 시간 오름차순 정렬
time.sort(key=lambda x:x[0])

# 첫번째 회의 끝나는 시간
x = time[0][1]

# 최대 회의 수 저장 변수
result2 = 1

for i in range(1,n):
  if x <= time[i][0]:
    # print(f"{x} <= {time[i][0]}")
    x = time[i][1]
    result2 +=1

if result1 > result2 :
  print(result1)
else:
  print(result2)