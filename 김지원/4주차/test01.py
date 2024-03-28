for i in range(4,-1,-1):
  for j in range(i):
    print(" ", end="")
  for k in range(0,5-i,1):
    print("*", end="") 
  print()