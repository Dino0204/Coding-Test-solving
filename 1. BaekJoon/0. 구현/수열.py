n , k = map(int,input().split())

arr = list(map(int,input().split()))

arrSum = [arr[0]]
arrSumK= []

# 1 -6 -13 -9 3 10 20 21 5
# -12 -12 -3 14 31 28

for i in range(1,n):
  arrSum.append(arr[i] + arrSum[i-1])

for i in range(k-1,n):
  if i < k:
    arrSumK.append(arrSum[i])
  else:
    arrSumK.append(arrSum[i] - arrSum[i-k])

maxTemperature = arrSumK[0]

for i in range(n-k+1):
  if maxTemperature < arrSumK[i]:
    maxTemperature = arrSumK[i]

# print(arrSum)
# print(arrSumK)
print(maxTemperature)
