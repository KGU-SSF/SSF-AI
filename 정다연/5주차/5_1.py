score = list(map(int, input().split()))

a=0
for n in score:
    if (n<50):
        n = 50
    a = a + n
    print (a)


mean = a/5
mean = int(mean)
print(mean)