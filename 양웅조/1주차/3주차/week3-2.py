G = float(input("enter your grade"))
if G > 100:
    print("enter again")

elif G < 0:
    print("enter again")

elif G >= 90:
    print("you are A")
elif G >= 80:
    print("you are B")
elif G >= 70:
    print("you are C")
elif G >= 60:
    print("you are D")
else:
    print("you are F")
