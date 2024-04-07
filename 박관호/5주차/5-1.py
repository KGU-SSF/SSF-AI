score_list = []
for i in range(1, 6):
    score = int(input(f'{i}번째 성적 입력 : '))
    if score % 5 == 0:
        if score < 50:
            score_list.append(50)
        else:
            score_list.append(score)

sum = 0
for j in range(0,len(score_list)) :
    sum += score_list[j]
avg = sum / len(score_list)
print(int(avg))