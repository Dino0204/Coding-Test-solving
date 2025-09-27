# - 기준으로 문자열 입력
arr = list(map(str,input().split('-')))

length = len(arr)

# + 가 문자열에 있다면 
for i in range(length):
  arr[i] = arr[i].split('+')
  
  lengthJ = len(arr[i])
  sum = 0
  
  for j in range(lengthJ):
    sum += int(arr[i][j])
  
  arr[i] = sum

sum = arr[0]

for i in range(1,length):
  sum -= arr[i]

print(sum)
