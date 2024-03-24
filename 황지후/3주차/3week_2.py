test = int(input("시험점수를 입력하시오 : "))

if test < 0 or test > 100:
    print ("다시 입력해주세요.")
    quit()

if 90<= test <= 100:
    print ("A") 

elif 80 <= test < 90:
    print ("B")

elif 70 <= test <80:
    print ("C")

elif 60 <= test < 70:
    print ("D")

else:
    print ("F")


