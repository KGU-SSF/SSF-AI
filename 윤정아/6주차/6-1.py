string=input()
if len(string)%2==0:
    m=(len(string))//2

else:
    m=(len(string)//2)+1
for i in range(m):
    if string[i]==string[-(i+1)]:
        i+=1
        return_="TRUE"
    else:
        return_="FALSE"
print(return_)
