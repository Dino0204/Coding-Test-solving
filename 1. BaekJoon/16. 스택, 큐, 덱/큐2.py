import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
  op = input().strip().split() 
  
  if op[0] == "push":
    queue.append(op[1])
    
  elif op[0] == "pop":
    if len(queue): 
      y = queue.popleft()
      print(y) 
    else: 
      print(-1)
    
  elif op[0] == "size":
    print(len(queue))
    
  elif op[0] == "empty":
    print(0) if len(queue) else print(1)
    
  elif op[0] == "front":
    print(queue[0]) if len(queue) else print(-1)
    
  elif op[0] == "back":
    print(queue[-1]) if len(queue) else print(-1)