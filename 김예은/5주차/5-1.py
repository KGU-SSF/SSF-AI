sum = 0
for i in range(5):
  a=int(input(""))
  if a<50:
    a = 50
  sum = sum + a

avg = int(sum/5)
print(avg)