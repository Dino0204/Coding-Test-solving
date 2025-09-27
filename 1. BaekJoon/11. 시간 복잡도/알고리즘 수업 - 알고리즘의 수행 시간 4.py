# MenOfPassion
# sum = 0
# for i in range(1, n):
#   for j in range(i+1,n+1):
#     sum = A[i] * A[j]
# return sum

# 시간복잡도 O(n * (n - 1) / 2)
n = int(input())
print(n * (n - 1) // 2)
print(2)