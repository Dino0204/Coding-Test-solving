# 전체 가로 m칸, 세로 n칸 크기의 땅
# 비옥도(k)는 각 칸에 0~99 사이의 숫자
# 교원이가 농사를 짓기 위해 골라야 하는 땅의 크기는 가로 x칸, 세로 y칸
# 구역 비옥도(ka)를 각 칸 의 비옥도(k)의 합으로 결정
m, n, x, y = map(int,input().split())

biokdo = []
results = []

def Biokdo(i, j):
  current_biokdo = 0 
  
  for i1 in range(y):
    for j1 in range(x):
      if 0 <= i + i1 < n and 0 <= j + j1 < m:
        current_biokdo += biokdo[i + i1][j + j1]

  return current_biokdo

for i in range(n):
  biokdo.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    # print(i,j, biokdo[i][j])
    results.append(Biokdo(i, j))

print(max(results))