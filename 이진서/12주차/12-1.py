input_data = 5 #input_data에 5 대입
weight = 3 #가중치에 3 대입
target = 8 #target에 8 대입
learning_rate = 0.1 #학습률에 0.1 대입

pred = weight * input_data

error = pred - target #오차를 예측값 - target으로 정의
print("original error", error)

slope = 2*input_data*error #오차함수의 기울기를 2*input_data*오차로 정의
print("slope", slope)

new_weight = weight-learning_rate*slope #새로운 가중치를 가중치 - 학습률*오차함수의 기울기로 정의
print("new weight", new_weight)

new_pred = new_weight*input_data #새로운 예측값을 새로운 가중치*input_data로 정의
print("new prediction", new_pred)

new_error = new_pred - target #새로운 오차를 새로운 예측값 - target으로 정의
print("new error:", new_error)
