input_data = 5
weight = 3
target = 8
learning_rate = 0.1

# 초기 예측값 계산 5X3=15
pred = weight * input_data
print(f"초기예측값: {pred}")

# 초기 오차 계산 15-8=7
error = pred - target
print(f"초기오차: {error}")

# 오차함수의 기울기 계산 2X5X(15-8)=70
gradient = 2 * input_data * (pred - target)
print(f"오차함수 기울기: {gradient}")

# 새로운 가중치 계산 3-0.1X70=-4
new_weight = weight - learning_rate * gradient
print(f"새로운 가중치: {new_weight}")

# 새로운 예측값 계산 -4X5=-20
new_pred = new_weight * input_data
print(f"새로운 예측값: {new_pred}")

# 새로운 오차 계산 -20-8=-28
new_error = new_pred - target
print(f"새로운 오차: {new_error}")