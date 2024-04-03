import sys

def play(yut):
    front = yut.count(0)
    back = yut.count(1)
    if (front == 1 and back == 3): 
        return 'A'
    elif (front == 2 and back == 2):
        return 'B'
    elif (front == 3 and back == 1):
        return 'C'
    elif (front == 4 and back == 0):
        return 'D'
    elif (front == 0 and back == 4):
        return 'E'

yut = []

for i in range(3):
    yut.append(list(map(int, sys.stdin.readline().split())))

for y in yut:
    print(play(y))



