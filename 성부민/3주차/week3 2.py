score = int(input("점수를 입력하시오:"))
if 0<=score<=100: 
  print(f"입력한 점수는 {score}입니다.")
  if score>=90:
    print("A")
  elif score>=80:
    print("B")
  elif score>=70:
    print("C")
  elif score>=60:
    print("D")
  else:
    print("F")
else:
  print("다시 입력해주세요.")