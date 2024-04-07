while True:
  score = int(input("시험 점수를 입력하세요: "))

  if score > 100 or score < 0:
    print("다시 입력해주세요.")
    continue

  if 90 <= score <= 100:
    print("A")
  elif 80<= score <=89:
    print("B")
  elif 70<= score <=79:
    print("C")
  elif 60<= score <=69:
    print("D")
  else:
    print("F")

  break

