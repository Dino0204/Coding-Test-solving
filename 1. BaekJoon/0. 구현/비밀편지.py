# n = int(input())
# jBin = input()
# result = ''


# abcd = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
# jBin = [jBin[i:i+6] for i in range(0,len(jBin),6)]

# for i in range(n):
#   falseCount = []
#   for j in range(8):
#     JBIN = list(jBin[i])
#     ABCD = list(abcd[j])
#     diff = [ai == bi for ai, bi in zip(JBIN, ABCD)]
#     falseCount.append(diff.count(False))


#   if 0 in falseCount:
#     result += (chr(65 +(falseCount.index(0))))
#   elif 1 in falseCount:
#     result += (chr(65 +(falseCount.index(1))))
#   else:
#     print(falseCount)
#     print(falseCount.index(2))
#     exit()
# print(result)

# 2.

n = int(input())
arr = input()

# 문자와 이진수 매핑
abcd = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
arr = [arr[i:i+6] for i in range(0, len(arr), 6)]

def FindChar(whatChr):
    result = ''
    
    for code in whatChr:
        match_found = False
        for i in range(len(abcd)):
            # 두 이진수 간의 차이를 계산
            diff_count = sum(1 for a, b in zip(code, abcd[i]) if a != b)
            
            if diff_count == 0:  # 완벽히 일치
                result += chr(65 + i)  # A~H에 해당하는 문자
                match_found = True
                break
            elif diff_count == 1:  # 1자리만 틀림
                result += chr(65 + i)
                match_found = True
                break
        
        if not match_found:  # 어떤 문자와도 매치되지 않음
            return len(result) + 1  # 현재까지 인식한 문자 개수 + 1
    
    return result

# 문자 테스트 케이스
result = FindChar(arr)
print(result)


