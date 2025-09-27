n = int(input())

honeys = list(map(int, input().split()))

# 9 9 4 1 4 9 9
# 9, 18, 22, 23, 27, 36, 45

max = 0
first_bee_idx = 0

for beehive_idx in range(n, -1, -1):  
  print(beehive_idx)
  
  for second_bee_idx in range(first_bee_idx + 1, n):
    if second_bee_idx > beehive_idx:
      second_bee_sum = sum(honeys[beehive_idx:second_bee_idx+1])
    else:
      second_bee_sum = sum(honeys[second_bee_idx+1:beehive_idx:])
    
    temp = honeys[first_bee_idx+1:beehive_idx]
    temp.pop(se)
    
    print(temp)
    
    # print(first_bee_sum, second_bee_sum)
    # result = first_bee_sum + second_bee_sum
    
    # if max < result:
    #   max = result

print(max)