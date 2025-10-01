n = int(input())

# 1,4,16,64,256... 4의 제곱수

# dp[1] = 1 SK
# dp[2] = 0 CY
# dp[3] = 1 SK
# dp[4] = 1 SK
# dp[5] = 0 CY

# dp[6] = 1 SK
# dp[7] = 0 CY
# dp[8] = 1 SK
# dp[9] = 1 SK
# dp[10] = 0 CY

# n % 5 == 2, 0

if n % 5 == 2 or n % 5 == 0:
  print("CY")
else:
  print("SK")