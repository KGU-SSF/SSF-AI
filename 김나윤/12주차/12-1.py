input_data = 5  # 입력 값 = 5
weight = 3  # 초기 가중치 = 3
target = 8  # 목표 값 = 8
learning_rate = 0.01  # 학습률 = 0.1

# pred = 예측값
pred = weight * input_data 

# error = 오차값
error = pred - target
print("original error:", error)

# slope = 기울기 / 기울기 계산 및 가중치 조정
slope = 2 * input_data * error
print("slope :", slope)

# new weight = 새로운 가중치
new_weight = weight - learning_rate * slope
print("new weight:", new_weight)

# new pred = 새로운 예측값 / 변경한 가중치로 새 예측값 계산
new_pred = new_weight * input_data
print("new prediction:", new_pred)

# new error = 새로운 오차값 / 새 예측값으로 새 오차값 계산
new_error = new_pred - target
print("new error :", new_error)


"""
< 실행 결과 >
original error: 7
slope : 70
new weight: 2.3
new prediction: 11.5
new error : 3.5

"""