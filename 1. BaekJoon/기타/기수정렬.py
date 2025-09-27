n = int(input())


# arr = list(map(int,input().split()))

# 백준 제출
# 리스트 컴프리헨션
# arr = []
# for i in range(n):
#   arr.append(int(input()))
arr = [int(x) for x in input().split()]

# 최대 자리수
radix = len(str(max(arr)))

t1 = 10
t2 = 1

for i in range(radix):
  # 버킷 초기화
  bucket = [[] for i in range(10)]
  for j in range(n):
    # 각 자리수마다 값 할당
    # print(f"{t2}의 자리수: {(arr[j] % t1) // t2} | 값: {arr[j]}")
    bucket[(arr[j] % t1) // t2].append(arr[j])
  
  # 버킷을 1차원 배열로 바꾼 후 원본 배열에 할당
  arr = sum(bucket,[])
  
  # print(f"{t2} 자리수의 버킷 : {bucket}")
  
  t1 *= 10
  t2 *= 10

# 결과
for i in range(n):
  print(arr[i])
