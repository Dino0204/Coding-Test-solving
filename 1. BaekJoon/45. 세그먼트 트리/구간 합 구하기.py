# n : 수의 개수 \ m : 수의 변경이 일어나는 횟수 \ k : 구간합을 구하는 횟수
n,m,k = map(int,input().split())

num = []
for i in range(n):
  num.append(int(input()))

segment_tree = [0 for _ in range(4*n)]

def build_tree(index,left,right):
  
  if left == right:
    segment_tree[index] = num[left]
  else:
    
    mid = (left + right) / 2
    
    left_node = build_tree(2*index,left,mid)
    right_node = build_tree(2*index + 1,mid + 1,right)
    segment_tree[index] = left_node + right_node
    
  return segment_tree[index]

def find_tree(b,c,index,left,right):
  
  if c < left or right < b:
    return 0
  


# a 1 | b번째 수를 c로 바꿈
# a 2 | b번째 수부터 c번째 수까지의 합을 구하고 출력
for i in range(k+m):
  a,b,c = map(int,input().split())
  
  if a == 1:
    k
  else:
    print(num2[c] - num2[b-1])
