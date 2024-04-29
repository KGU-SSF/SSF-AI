J=int(input("준서의 성능을 입력하세요:"))
E=int(input("이다의 성능을 입력하세요:"))
H=int(input("준서의 성능을 입략하세요:"))
WJ=int(input("우진의 성능을 입력하세요:"))
WH=int(input("우현의 성능을 입력하세요:"))

if  J<50:
    J=50
if  E<50:
    E=50
if  H<50:
    H=50
if  WJ<50:
    WJ=50
if  WH<50:
    WH=50


s=(J+E+H+WJ+WH)//5
print(s)