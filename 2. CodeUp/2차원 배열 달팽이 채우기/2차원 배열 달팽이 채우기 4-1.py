n,m = map(int,input().split())


arr = [[0 for _ in range(m)] for _ in range(n)]
arr[0][0] = 1

num = 1
i,j = 0,0
direction = 1



while True:

  # if i == j:
  #   print(num)
  
  if num >= n * m:
    break
  
  
  # 오른쪽
  if direction == 1:
    # 0을 제외한 수가 있거나 범위를 넘어갔다면
    if j + 1 >= m or (1 <= arr[i][j + 1] <= n * m):
      # print("오른쪽 끝")
      i += 1
      direction = 2
    else:
      j += 1
  # 아래쪽
  elif direction == 2:
    # 0을 제외한 수가 있거나 범위를 넘어갔다면
    if i + 1 >= n or (1 <= arr[i + 1][j] <= n * m):
      # print("아래쪽 끝")
      j -= 1
      direction = 3
    else:
      i += 1
  # 왼쪽
  elif direction == 3:
    # 0을 제외한 수가 있거나 범위를 넘어갔다면
    if j - 1 < 0 or (1 <= arr[i][j - 1] <= n * m):
      # print("왼쪽 끝")
      i -= 1
      direction = 4
    else:
      j -= 1
  elif direction == 4:
    # 0을 제외한 수가 있거나 범위를 넘어갔다면
    if i - 1 < 0 or (1 <= arr[i - 1][j] <= n * m):
      # print("위쪽 끝")
      j += 1
      direction = 1
    else:
      i -= 1
  
  
  num += 1
  arr[i][j] = num

for i in range(n):
  for j in range(m):
    print(arr[i][j],end=" ")
  print()




