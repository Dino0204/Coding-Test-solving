# 후위 표기식
postfix = input().split()

stack = []

for i in range(len(postfix)):
  # print(f"{i}: {stack}")
  try:
    stack.append(int(postfix[i]))
  except ValueError as error:
    exp = postfix[i]
    if exp != " ":
      # print(f"current stack: {stack}")
      prev_num = stack.pop()
      next_num = stack.pop()
      
      if exp == "+": result = next_num + prev_num
      elif exp == "-": result = next_num - prev_num
      elif exp == "*": result = next_num * prev_num
      # print(f"result: {next_num} {exp} {prev_num} = {result}")
      
      stack.append(result)
      
      # exit()

print(stack[0])