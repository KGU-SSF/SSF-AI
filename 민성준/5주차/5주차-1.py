sum = 0

def lowscore(a):
    if a < 50:
        a = 50
    return a

for i in range(5):
    a = int(input())
    a = lowscore(a)
    sum += a

print(int(sum/5))