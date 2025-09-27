import sys
input = sys.stdin.readline

# N : arr 의 원소 수 / M : 구간 합의 수
N , M = map(int,input().split())

# 5 4 3 2 1
arr = list(map(int,input().split()))
arrSum = [0]

# 0 : 0 ~ 0 / 1 : 0 ~ 1... 0 ~ n
# 0 5 9 12 14 15
for i in range(N):
  arrSum.append(arr[i] + arrSum[i]) 

# i ~ j 까지의 합
for t in range(M):
  I , J = map(int,input().split())

  result = arrSum[J] - arrSum[I-1]
  print(result)