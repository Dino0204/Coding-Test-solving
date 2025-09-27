n,m = map(int,input().split())

arr = list(map(int,input().split()))


arrSum = [0]
arrRemain = [0]
arrRCount = [0 for _ in range(m)]

for i in range(1,n+1):
  arrSum.append(arr[i-1] + arrSum[i-1])
  arrRemain.append(arrSum[i]%m)


for i in range(1,n+1):
  arrRCount[arrRemain[i]] += 1

result = arrRCount[0]

# (A+B) % C == (A%C) + (B%C)
# (A-B) % C == (A%C) - (B%C)
for i in range(m):
  result += ( arrRCount[i]*(arrRCount[i] - 1) ) // 2

# print(arrRemain)
# print(arrRCount)

print(result)






# 7 - 1 | 3 / 6 / 9 | 6 - 3 / 9 - 3 / 9 - 6
# 1 - 1 0 - 0 0 - 0 0 - 0 | 0 0 0 
# 나머지끼리 빼서 0이 되는 경우의 수 + 0의 수



# 0 | 1 3 6 7 9
# 0 | 1 0 0 1 0

# 0 : 6 | 1 : 1

# 0 | 1 3 6 7 9 13 15 16 17 20
# 0 | 1 0 0 1 0  1  2  1  2  2

# 0 : 6 | 1 : 6 | 2 : 3


# for i in range(1,n+1):
#   if arrRemain[i] == 0:
#     # print(f'{arrRemain[i]} = 0')
#     result += 1
  
#   for j in range(i+1,n+1):
#     if arrRemain[i] - arrRemain[j] == 0:
#       # print(f'{arrRemain[i]} - {arrRemain[j]} = 0') 
#       result += 1