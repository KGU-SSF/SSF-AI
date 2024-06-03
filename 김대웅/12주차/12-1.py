input_data = 5
weight = 3
target = 8 
learing_rate = 0.1 #데이터는 5, 가중치는 3, 목표값은 8, 학습률은 0.1로 설정

pred = weight * input_data #예측값을 설정, pred = 3 x 5 = 15

error = pred - target
print("error", error) #오차를 계산함, error= 15 - 8 = 7

slope = 2 * input_data * error  
print("slope", slope) #기울기를 계산함, slope = 2 x 5 x 7 = 70

new_weight =  weight - learing_rate * slope  
print("new weight", new_weight) #새로운 가중치를 구함, new_weight = 3 - 0.1 x 70 = -4

new_pred= new_weight * input_data  
print("new pred", new_pred) #새로운 가중치 이용해서 예측값을 계산함, new_pred = -4 x 5 = -20

new_error = new_pred - target 
print("new error", new_error) #새로운 오차를 계산함, new_error = -20 - 8 = -28