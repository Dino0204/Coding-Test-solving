n = int(input())

num = list(map(int,input().split()))
num.sort()
m = int(input())

findList = list(map(int,input().split()))

def binary_search(left, right, key):
  mid = (left + right)//2
  
  if left < right:
    if key == num[mid]:
      return 1
    elif key < num[mid]:
      return binary_search(left,mid,key)
    elif key > num[mid]:
      return binary_search(mid+1,right,key)
  else:
    return 0

for i in range(m):
  print(binary_search(0,n,findList[i]))

# 이분 탐색
# mid == key return 1
# mid >  key 
# mid <  key
