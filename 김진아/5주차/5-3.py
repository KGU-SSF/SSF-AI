result1 = input()
result2 = input()
result3 = input()

rcount1 = result1.count('0')
rrcount1 = 4 - rcount1

rcount2 = result2.count('0')
rr_count2 = 4 - rcount2

rcount3 = result3.count('0')
rrcount3 = 4 - rcount3

def print_result(rcount):
    if rcount == 1:
        print("A")
    elif rcount == 2:
        print("B")
    elif rcount == 3:
        print("C")
    elif rcount == 4:
        print("D")
    else:
        print("E")

print_result(rcount1)
print_result(rcount2)
print_result(rcount3)