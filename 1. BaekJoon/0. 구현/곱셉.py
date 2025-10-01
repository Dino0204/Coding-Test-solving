a = int(input())
b = list(input())

# 뒷자리부터 각 자리수마다 곱셈 계산
for i in range(len(b)-1, -1, -1):
    # 현재 자리수의 숫자
    digit = int(b[i])
    # a와 현재 자리수의 숫자를 곱한 결과 출력
    print(a * digit)

# 최종 결과 계산
result = a * int(''.join(b))
print(result)
