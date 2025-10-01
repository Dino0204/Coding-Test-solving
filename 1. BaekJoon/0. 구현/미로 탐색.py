from queue import Queue

n, m = map(int, input().split())

# # 띄어쓰기나 구분자가 없는 입력의 경우
maze = [list(map(int, input().strip())) for _ in range(n)]

# 동, 서, 남, 북
position = [
  (1, 0),
  (-1, 0),
  (0, 1),
  (0, -1)
]

print(maze) 
print()

def FFW(x, y):  
  visited = set({(x, y)})
  queue = Queue()
  queue.put((x, y))

  while not queue.empty():
    print(queue.queue)
    v = queue.get()
    # print(visited)
    # print(v)
    
    for p in position:
      is_in_range = (0 <= v[0] + p[0] < n and 0 <= v[1] + p[1] < m)
      isnt_visited = (v[0] + p[0], v[1] + p[1]) not in visited
      is_one = maze[x + p[0]][y + p[1]] == 1
      
      print(is_in_range, isnt_visited, is_one)
      print(v[0] + p[0], v[1] + p[1])
      
      if is_in_range and isnt_visited and is_one:
        queue.put((v[0] + p[0], v[1] + p[1]))
        visited.add((v[0] + p[0], v[1] + p[1]))

FFW(0, 0)
