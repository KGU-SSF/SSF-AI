input_data=5
weight=3
target=8
learning_rate=0.1
pred=weight*input_data


#오차: pred=3*5=15
#error=15-8=7
error = pred - target
print("original error:", error)


#오차 함수의 기울기
# 2*5*7=70
slope = 2 * input_data * error
print("slope:", slope)

#새로운 가중치
#3 - 0.1 * 70 = 3-7 = -4
new_weight = weight - learning_rate * slope
print("new weight:", new_weight)


#새로운 예측값
# -4*5= -20
new_pred = new_weight * input_data
print("new prediction:", new_pred)

#새로운 오차
# -20-8 = -28
new_error = new_pred - target
print("new error:", new_error)