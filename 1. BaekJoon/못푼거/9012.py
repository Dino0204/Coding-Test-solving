# t = int(input())

# arr = []
# top = -1
# left = 0

# for i in range(t):
#   arr.append(list(input()))

# # arr 길이 구하기
# row_lengths = [len(row) for row in arr]
# print(row_lengths)

# # def push(top,element):
# #   stack[top] = element

# # def pop(top,element):
  

# # arr is VPS?
# for i in range(t):
#   stack = [0 for i in range(row_lengths[i])]

#   for j in range(row_lengths[i]):
    
#     # !isFUll
#     if arr[i][j] == '(' and not(top == row_lengths[i] - 1):
#       top += 1
#       left += 1
#       push(top,arr[i][j])
    
#     # !isEmpty
#     elif arr[i][j] == ')' and not(top == -1):
      
#       pop()
#       left -= 1
#       top -= 1
  
#   print(len(stack))
#   print(stack)
  