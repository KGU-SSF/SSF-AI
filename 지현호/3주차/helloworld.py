'''
#1번

a, b=input("출력값: ").split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
'''

'''
#2번

a=input("시험점수: ")
a=float(a)
if 90<=a<=100:
    print("A")
if 80<=a<=89:
    print("B")
if 70<=a<=79:
    print("C")
if 60<=a<=69:
    print("D")
elif 89<a<90:
    print("F")
elif 79<a<80:
    print("F")
elif 69<a<70:
    print("F")
elif 0<=a<=60:
    print("F")
else:
    print("다시 입력해주세요")
'''


'''
#3번

aaaa = input("입력: ")

for s in range(len(aaaa)):
    if aaaa[s] == "[":
        aa = aaaa[s:len(aaaa)]

vv = aa[1:len(aa)-1]
aa = vv.split(",")

rdtc = []

for d in aa:
    if int(d) % 2 == 1:
        rdtc.append(int(d))

print(rdtc)
'''

'''
qqq = input("입력예시: ")

for qq in range(len(qqq)):
    if qqq[qq] == "[":
        bb = qqq[qq:len(qqq)]

nn = bb[1:len(bb)-1]
bb = nn.split(",")

bbbb = len(bb)

print(bbbb)
'''