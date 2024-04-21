rotator = input("회문을 입력하세요:")
li = list(rotator)
li.reverse()
rotated = ''.join(li)
if rotator == rotated :
    print(True)
else :
    print(False)
