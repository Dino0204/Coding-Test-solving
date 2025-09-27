# 주스의 양 입력 받기
A, B, C = map(int, input().split())

# 칵테일 비율 입력 받기
I, J, K = map(int, input().split())

# 각 주스별로 만들 수 있는 칵테일의 수 계산
# 각 주스를 해당 비율로 나누어 최소값을 구함
cocktails = min(A/I, B/J, C/K)

# 남은 주스의 양 계산
remaining_A = A - (cocktails * I)
remaining_B = B - (cocktails * J)
remaining_C = C - (cocktails * K)

# 결과 출력 (소수점 6자리까지)
print(f"{remaining_A:.6f} {remaining_B:.6f} {remaining_C:.6f}")