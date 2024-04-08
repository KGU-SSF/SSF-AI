#1. 평균 성능 출력 프로그램
list1=['준서','이다','홍다','우진','우현']
sum=0
for i in range(5):
    performance=int(input("%s의 성능 입력 : "%list1[i]))
    if performance < 50:
        performance=50
    sum+=performance

print(sum//5) 
