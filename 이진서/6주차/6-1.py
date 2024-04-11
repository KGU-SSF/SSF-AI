s = input()

l = list(s)

if len(l)%2 == 0:
    print("False")
elif len(l)%2 != 0:
    if l[-1] == l[0] and l[1] == l[-2]:
        print("True")
    elif l[-1] != l[0] or l[1] != l[-2]:
        print("False")


