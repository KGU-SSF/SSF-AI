num_scores = int(input("몇 개의 성능 입력하시겠습니까? "))
scores = []
for i in range(num_scores):
    score = input(f"{i+1}번째 성능을 입력하세요: ")
    score = 50 if int(score) < 50 else int(score)
    scores.append(score)
average = sum(scores) / len(scores)
print(f"입력하신 성능들의 평균은 {average:f}입니다.")
