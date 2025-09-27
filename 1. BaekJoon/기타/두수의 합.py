n = int(input())

numArr = list(map(int,input().split()))

x = int(input())

# 누적합을 구하기 위해서 sort
numArr.sort()
# print(numArr)

length = len(numArr) - 1

lPointer = 1 - 1
rPointer = length
cnt = 0


while True:
  if rPointer <= lPointer:
    break
  
  result = numArr[lPointer] + numArr[rPointer]
  
  # 같을 때
  if result == x:
    # print(f"=|{numArr[lPointer]} + {numArr[rPointer]} = {result} | {cnt}")
    cnt += 1
    lPointer += 1
  
  # 클 때
  if result > x:
    # print(f">|{numArr[lPointer]} + {numArr[rPointer]} = {result} | {cnt}")
    rPointer -= 1
    
  # 작을 때
  if result < x:
    # print(f"<|{numArr[lPointer]} + {numArr[rPointer]} = {result} | {cnt}")
    lPointer += 1
  


print(cnt)