# 파일을 완전 삭제하는 방법
# 삭제할 파일을 n번 덮어 씌운다.
# 0 -> 1 , 1 -> 0으로

n = int(input())
bit1 = list(input())
bit2 = list(input())

diff = [b1 != b2 for b1, b2 in zip(bit1, bit2)]

if (n % 2 == 0 and bit1 == bit2) or (n % 2 != 0 and diff.count(True) == len(bit1)):
  print("Deletion succeeded")
else:
  print("Deletion failed")