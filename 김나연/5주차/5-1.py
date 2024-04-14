n_list = []
for i in range(5):
  n_list.append(int(input("성능을 입력하세요:")))

result = []
for i in n_list:
  if i < 50:
    result.append(50)
  else:
    result.append(i)

avg = sum(result) / len(result)
print(int(avg))
