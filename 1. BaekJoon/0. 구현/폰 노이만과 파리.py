# 기차의 속도 S,  
# 파리의 속도 T, 
# 처음 두 기차 사이의 거리 D

s,t,d = map(int,input().split())

print((d // (s * 2) ) * t) 
