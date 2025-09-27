# # 수의 개수  n
# n = int(input())
# arr = list(map(int,input().split()))

# arr.sort()
# print(arr)

# def Good (arr , left , right , good):
#   if left == right :
#     print(f"예외 : {left} == {right}")
#     right += 1
    

#   if arr[left] + arr[right] == arr[good]:
#     print(f"함수 : {arr[left]} + {arr[right]} == {arr[good]}")
#     result = True
#   else :
#     print(f"함수 : {arr[left]} + {arr[right]} != {arr[good]}")
#     result = False

#   return result

# # 주의 ) 항상 l r good 순서여야 함
# l = 0
# r = 1
# good = 2
# goodCount = 0

# while True :
  
#   # 종료조건 (탐색하는 좋은 수가 값을 idx 값을 넘어섰을 때)
#   if good >= n:
#     print(f"종료 : {good} >= n")
#     break
  
#   # 서로 다른 수 두개의 합
#   is_Good = arr[l] + arr[r]
#   #print(f"두 수의 합 : {is_Good}")
  
#   # 같을 때
#   if is_Good == arr[good] :
#     print(f"좋다 : {is_Good} == {arr[good]} | {goodCount + 1}")
  
#     # 다음 수로 넘어가기
#     good += 1
#     goodCount += 1
  
#   # 클 때 (더 해서 큰 경우)
#   elif is_Good > arr[good] :
#     print(f"{is_Good} >  {arr[good]}")
    
#     # l을 줄이는 경우

#     if Good(arr, l - 1 , r , good) :
#       l -= 1
#     # r을 줄이는 경우
#     elif Good(arr, l , r - 1 , good) :
#       r -= 1
#     # 빼서 작은 값을 탐색해도 없는 경우 (클 때 하나를 줄였는데 작은 값이 나온 경우)
#     else :
#       good += 1
    
#   # 작을 때 (l : r 둘 중 뭘 올려야 할까 고민)
#   elif is_Good < arr[good] :
#     print(f"{is_Good} <  {arr[good]}")
    
#     # l을 올리는 경우
#     if Good(arr, l + 1 , r , good) :
#       l += 1
#     # r을 올리는 경우
#     elif Good(arr, l , r + 1 , good) :
#       r += 1
#     else :
#       good += 1

# print(goodCount)

# 알고리즘
# 자료구조
# 정렬
# 이분 탐색
# 두 포인터

# 문제
# N개의 수에서 어떤 수가 다른 수 두개의 합으로 나타낼 수 있다면 그 수를 "좋다"고 한다.

n = int(input())
is_Good = [False for _ in range(n)]
arr = list(map(int,input().split()))
arr.sort()

for i in range(n):
  l = 0
  r = n - 1
  while l < r:
    
    # l 과 r이 i와 같은 경우는 넘어가기
    if l == i:
      l += 1
    if r == i:
      r -= 1

    # l과 r이 i와 다른 경우 & l과 r이 같지 않은 경우
    if l != r:
      # l와 r이 가리키는 값의 합이 i와 같은 경우
      if arr[l] + arr[r] == arr[i]:
        is_Good[i] = True
        break
      # l와 r이 가리키는 값의 합이 i보다 작은 경우
      elif arr[l] + arr[r] < arr[i]:
        l += 1
      # l와 r이 가리키는 값의 합이 i보다 큰 경우
      else:
        r -= 1

# print(arr)
# print(is_Good)
print(is_Good.count(True))