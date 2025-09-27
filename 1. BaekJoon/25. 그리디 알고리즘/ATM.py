# 1 ~ N
n =  int(input())

# 각각의 사람의 인출 시간
arr1 = list(map(int,input().split()))

# 인출 시간 오름차 순으로 정렬
arr1.sort()

# 인덱스 오류 방지
arr2 = [0]

sum = 0 

# 누적 합
for i in range(n):
  arr2.append(arr1[i]+arr2[i])
  sum += arr2[i]

# 마지막 수 더해주기
print(sum + arr2[n])

