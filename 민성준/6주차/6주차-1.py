def reStr(a):
    ar = ""
    for i in a:
        ar = i + ar
    return a == ar

print(reStr(str(input())))

