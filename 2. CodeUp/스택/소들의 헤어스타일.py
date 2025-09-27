n = int(input())

cow_height = []
cnt = 0

for i in range(n):
  cow_height.append(int(input()))

# for i in range(n):
#   for j in range(i + 1, n):
    
#     if cow_height[i] <= cow_height[j]:
#       break
    
#     cnt += 1

# print(cnt)

# 여기서 스택을 어떻게 이용할 수 있을까?
# 10 3 7 4 12 2

# 순서대로 스택으로 탐색하는 경우
# 10 3 7 4 break
# 3 break
# 7 4 break
# 12 2 break
# 2 break
# -> 이중 for문이랑 차이가 없음

# 역순으로 스택을 탐색하는 경우
# 2 break
# 12 2 break
# 4 break 12 2 
# 7 4 break 12 2 
# 3 break 7 4 12 2
# 10 3 7 4 break 12 2

stack = []
cow_height.reverse()
i = 0
top = -1

while True:
  if stack[i] <= stack[top]:
    stack.append(cow_height[i])
    i += 1

