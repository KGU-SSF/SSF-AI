w=str(input())
for i in range(len(w)//2):
    if w[i]!=w[-1-i]:
       print('false')
    else:
        print('true')
    break