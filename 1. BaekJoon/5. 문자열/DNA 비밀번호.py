# 문자열 길이, 부분문자열 길이
s,p = map(int,input().split())

# DNA 배열
dna = list(str(input()))

# 각각의 갯수
numA, numC, numG, numT = map(int,input().split())

# l,r 포인터
lPoint = 1 - 1
rPoint = p - 1

# A C G T
cntStr = [0 for i in range(4)]


# 더하기
def CountChangeStr(Point):
  # print(f"{dna[Point]} += 1")
  if dna[Point] == 'A':
    cntStr[0] +=1
  elif dna[Point] == 'C':
    cntStr[1] +=1
  elif dna[Point] == 'G':
    cntStr[2] +=1
  elif dna[Point] == 'T':
    cntStr[3] +=1

# 빼기
def MinusChangeStr(Point):
  # print(f"{dna[Point]} -= 1")
  if dna[Point] == 'A' and cntStr[0] > 0:
    cntStr[0] -=1
  elif dna[Point] == 'C' and cntStr[1] > 0:
    cntStr[1] -=1
  elif dna[Point] == 'G'  and cntStr[2] > 0:
    cntStr[2] -=1
  elif dna[Point] == 'T'  and cntStr[3] > 0:
    cntStr[3] -=1

# 부분문자열 초기 카운트
for i in range(p):
  CountChangeStr(i)

result = 0

while True:  
  if cntStr[0] >= numA and cntStr[1] >= numC and cntStr[2] >= numG and cntStr[3] >= numT:
    # print(cntStr)
    result += 1
  if rPoint == s - 1:
    break
  
  MinusChangeStr(lPoint)
  
  rPoint += 1
  lPoint += 1

  CountChangeStr(rPoint)

print(result)