n,m = map(int,input().split())
arr = [[0 for _ in range(m)]for _ in range(n)]

x = 0
num = 1

for k in range(n*m):
  for i in range(n):
    for j in range(m-1,-1,-1):
      if i + j == k:
        arr[i][j] = num
        num += 1


for i in range(n):
  for j in range(m-1,-1,-1):
    print(arr[i][j],end=" ")
  print("")