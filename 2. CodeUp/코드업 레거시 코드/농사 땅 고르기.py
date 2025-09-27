m,n,x,y = map(int,input().split())

biokdoCpy = []
biokdo = [[0 for i in range(m+2)]for j in range(n+2)]

kaAll = [[0 for i in range(m+2)]for j in range(n+2)]
ka = 0

# 입력받기
for i in range(n):
  biokdoCpy.append(list(map(int,input().split())))

# 복사하기
for i in range(1,n+1):
  for j in range(1,m+1):
    biokdo[i][j] = biokdoCpy[i-1][j-1]


# 땅 한칸씩 옮기기
  # 그 주변 x * y 비옥도 더하기
for i in range(1,n+1):
  for j in range(1,m+1):
    for k in range(i,i+y):
      for l in range(j,j+x):
        if (k <= n) and (l <= m):
          ka += biokdo[k][l]
        
    kaAll[i][j] = ka
    ka = 0
    


# 출력하기
Max_biokdo = kaAll[0][0]
for i in range(1,n+1):
  for j in range(1,m+1):
    if kaAll[i][j] > Max_biokdo:
      Max_biokdo = kaAll[i][j]

print(Max_biokdo)
