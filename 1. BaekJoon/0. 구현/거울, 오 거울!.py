while True:
  mirror = input()
  
  if mirror == "***":
    break
  else:
    rorrim = list(mirror)
    
    for i in range(len(mirror)-1,-1,-1):
      print(rorrim[i],end="")
    print()