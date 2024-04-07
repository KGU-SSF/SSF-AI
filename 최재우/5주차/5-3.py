for i in range(3):
  a = list(map(int, input().split()))
  if a.count(0) == 1:
    print("a")
  elif a.count(0) == 2:
    print("b")
  elif a.count(0) == 3:
    print("c")
  elif a.count(0) == 4:
    print("d")
  else:
    print("e")
    
    
