# [ i번째 줄의 문장은 문장의 첫 번째 글자에서 시작하여 i칸씩 건너뛰며 읽어야 한다 ]

i = 0

while True:
  str = input()
  i += 1  
  if str == "Was it a cat I saw?":
    break
  arr = list(str)
  for j in range(0,len(str),i+1):
    print(str[j],end="")
  print()
