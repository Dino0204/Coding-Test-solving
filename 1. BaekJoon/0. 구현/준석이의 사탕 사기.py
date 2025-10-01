n = int(input())

arr = list(map(int,input().split()))

arr.sort() 

result = sum(arr)

minNum = 0

for i in range(n):
  if arr[i] % 2 != 0:
    minNum = arr[i]
    break

if result % 2 == 0:
  print(result)
elif (result - minNum) % 2 == 0:
  print(result - minNum)
else:
  print(0)
