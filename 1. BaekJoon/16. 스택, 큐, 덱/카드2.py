from collections import deque

n = int(input())


cards = [i for i in range(1,n+1)]
queue = deque(cards)

for i in range(n-1):
  queue.popleft()
  tmp = queue.popleft()
  
  queue.append(tmp)
  
print(queue[0])