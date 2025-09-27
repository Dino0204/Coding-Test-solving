a = int(input())
b = int(input())

stack = []

x = 10
sum = 0
next_digit = 0
length = len(str(max(a,b)))

# 뒤부터 더하는데 몫을 다음 수로 나머지를 스택으로
for digit in range(length):  
  # a의 각 자리 
  digit1 = (a % x) // (x // 10)
  
  # b의 각 자리
  digit2 = (b % x) // (x // 10)
  
  # 각 자리끼리 더한 수
  sum = digit1 + digit2 + next_digit
  
  # 받아올림 수
  next_digit = sum // 10
  
  # 나머지 저장
  stack.append(sum if digit == length - 1 else sum % 10)
  
  x *= 10

if not stack:
  print(0)

for i in range(len(stack) - 1, -1, -1):
  print(stack.pop(), end="")