from collections import deque

n, k = map(int,input().split())

yose = [i for i in range(1, n+1)]
queue = deque(yose)
result = []
cnt = 0

while queue:
  cnt += 1
  tmp = queue.popleft()
  
  if cnt % k == 0:
    result.append(tmp)
  else:
    queue.append(tmp)

print("<",end="")
print(*result, sep=", ",end="")
print(">",end="")