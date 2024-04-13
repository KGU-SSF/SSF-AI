for i in range(3):
  a = list(map(int,input().split()))
  if a.count(0) == 1:
    print("A")
  elif a.count(0) == 2:
    print("B")
  elif a.count(0) == 3:
    print("C")
  elif a.count(0) == 4: 
    print("D")
  else:
    print("E")