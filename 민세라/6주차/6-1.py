s = list(input())
result = "True"
if(len(s)%2==1):
    c = len(s)//2
    s.remove(s[c])

for i in range(1,c):
    if(s[i-1] != s[-i]):
        result = "False"
        break

print(result)