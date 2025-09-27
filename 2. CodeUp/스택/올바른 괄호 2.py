# 올바른 괄호 문자열 판단
# 1. 여는 괄호와 닫는 괄호의 짝이 맞음
# 2. 포함 관계에 문제가 없음

# x )()(
# o ((()()))

# (((
# )
# (((
# )))

brackets = input()
stack = []

if brackets[0] == ")":
  print("bad") 
  exit()

for i in range(len(brackets)):
  # print(f"{i}: {stack}")
  if brackets[i] == "(":
    stack.append(brackets[i])
  elif brackets[i] == ")":
    if not stack:
      print("bad")
      exit()
    stack.pop()

if stack:
  print("bad")
else:
  print("good")