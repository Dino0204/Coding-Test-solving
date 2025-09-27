while True:
  str = input()
  
  if str == "#":
    break
  else:
    # lower -> 소문자로 변환,
    # vowel -> 모음, 
    # vowel에 'a','e','i','o','u' 각각 대입하여 count
    engCnt = sum(str.lower().count(vowel) for vowel in 'aeiou')
    print(engCnt)
