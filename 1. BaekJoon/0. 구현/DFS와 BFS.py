from collections import deque

# 정점 개수, 간선 개수, 시작 정점
n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(n + 1):
  graph[i].sort()

def dfs(v: int, visited: list[bool]):
  visited[v] = True
  print(v, end=" ")
  
  for w in graph[v]:
    if visited[w] == False:
      dfs(w, visited)


def bfs(v: int):
  visited = set({v})
  queue = deque([v])
  
  while queue:
    v = queue.popleft()
    print(v, end=" ")
    
    for w in graph[v]:
      if w not in visited:
        queue.append(w)
        visited.add(w)

dfs(v, [False] * (n + 1))
print()
bfs(v)