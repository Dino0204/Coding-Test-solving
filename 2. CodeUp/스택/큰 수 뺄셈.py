# 각 자릿수끼리 연산
# 만약 현재 연산이 음수라면?
  # 현 연산에 10을 더해서 계산
  # 다음 연산에 1을 빼서 계산

# 만약 첫번째 값이 0이라면
  # 다음 수가 1 이상의 수일 때까지 제거

a = int(input())
b = int(input())

stack = []

x = 10
isMinus = False
isBig = False
length = len(str(max(a,b)))

if a == b:
  print(0)
  exit()

if b > a:
  a , b = b, a
  isBig = True

for i in range(length):  
  # a의 각 자리 
  digit1 = (a % x) // (x // 10)
  
  # b의 각 자리
  digit2 = (b % x) // (x // 10)
  
  if isMinus:
    digit1 -= 1
    isMinus = False
  
  result = digit1 - digit2
  
  # 자릿수 계산
  if result < 0:
    # 음수일 경우
    stack.append(result + 10)
    isMinus = True
  else:
    stack.append(result)
  
  x *= 10

if not stack:
  print(0)


for i in range(len(stack)-1, -1, -1):
  # print(f"current {i}: {stack[i]}")
  if stack[i] == 0:
    # print(f"prev: {stack}")
    stack.pop()
    # print(f"next: {stack}")
  else:
    break

stack.reverse()

if isBig:
  print("-",end="")

for i in range(len(stack)):
  print(stack[i], end="")