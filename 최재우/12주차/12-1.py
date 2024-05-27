input_data = 5
weight = 3
target = 8 
learing_rate = 0.1 #초기값 설정, 입력 데이터는 5, 가중치는 3, 답은 8, 학습 빈도는 0.1만큼

pred = weight * input_data #예측값 구하기

error = pred - target
print("error", error) #오차 구하기

slope = 2 * input_data * error  
print("slope", slope) #기울기 구하기

new_weight =  weight - learing_rate * slope  
print("new weight", new_weight) #새로운 가중치 구하기

new_pred= new_weight * input_data  
print("new pred", new_pred) #새 가중치 이용한 예측값 계산

new_error = new_pred - target 
print("new error", new_error) #새 오차 계산