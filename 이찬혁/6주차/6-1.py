def hoimoon(strin):
    str = strin
    strlength = len(str) - 1
    for i in range(0,int(strlength/2)):
        if str[i] != str[strlength-i]:
            return False
    return True

a = input()
print(hoimoon(a))