def check(string):
    s = string.lower()
    for i in range(0,len(s)//2):
        if s[i] != s[-(i+1)]:
            return "False"
    return "True"

string1 = "level"
string2 = "rotator"
string3 = "hello"

print(check(string1))
print(check(string2))
print(check(string3))
