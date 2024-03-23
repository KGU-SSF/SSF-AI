# SSF 인공지능 스터디 3주차 과제



# 1번 ---------------

A, B = map(int, input("두 자연수 입력 : ").split())
print(A+B, A-B, A*B, A//B, A%B)

print()



# 2번 ---------------

score = int(input('시험 점수 입력 : '))
if score >= 90 and score <= 100 :
    print('A')
if score >= 80 and score < 90 :
    print('B')
if score >= 70 and score < 80 :
    print('C')
if score >= 60 and score < 70 :
    print('D')
if score < 60 and score >= 0 :
    print('F')
if score < 0 or score > 100 :
    print('다시 입력해주세요')

print()



# 3번 ---------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[:1]+nums[2:3]+nums[4:5]+nums[6:7]+nums[8:9])

print()



# 4번 ---------------

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))


