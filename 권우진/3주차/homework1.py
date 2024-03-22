
# 1번
def question1():
    a, b = input("a b: ").split()

    a = int(a)
    b = int(b)

    print(a + b, a - b, a * b, a // b, a % b)

# 2번
def question2():
    score = int(input("점수: "))

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score < 60:
        print("F")
    else:
        print("다시 입력해주세요")

# 3번
def question3():
    tmp = 0
    result = []

    li = input("리스트: ")

    for i in range(len(li)):
        if li[i] == "[":
            tmp = i
            break

    strings = li[tmp + 1:len(li) - 1]
    tmp_li = strings.split(",")

    for i in range(len(tmp_li)):
        if int(tmp_li[i]) % 2 == 1:
            result.append(int(tmp_li[i]))

    print(result)

# 4번
def question4():
    li = input("리스트: ")

    for i in range(len(li)):
        if li[i] == "[":
            tmp = i
            break

    strings = li[tmp + 1:len(li) - 1]
    tmp_li = strings.split(",")
    
    print(len(tmp_li))

if __name__ == "__main__":
    question1()
    question2()
    question3()
    question4()
