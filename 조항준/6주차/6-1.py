value = input("문자입력 : ")
length = len(value)

for i in range (0,length//2):
    if value[i] == value[-1-i]:
        print("True")
        break
    else:
        print("False")
        break
