score = int(input('점수 입력:'))
if score > 100: 
  print("다시 입력해주세요")
elif score >= 90:
  print('A')
elif score >= 80:
  print('B')
elif score >= 70:
  print('C')
elif score >= 60:
  print('D')
elif score < 0: 
  print("다시 입력해주세요")
else:
  print('F')