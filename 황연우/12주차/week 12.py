input_dada = 5 #입력값
weight = 3 #가중치
target = 8 #목표값
learning_rate = 0.1 #학습률

pred = weight * input_dada # 예측값(3*5)

error = pred - target #오차(15-8)
print("original error:", error) #결과(7)

slope = 2 * input_dada * error #오차함수의 기울기(2*5*7)
print("slope:", slope) #결과(70)

nwe_weight = weight - learning_rate * slope #새로운 가중치(3-0.1*70)
print("new weight:", nwe_weight) #결과(-4)

new_pred = nwe_weight * input_dada #새로운 예측값(-4*5)
print("new prediction:", new_pred) #결과(-20)

new_error = new_pred - target #새로운 오차(-20-8)
print("new error:", new_error) #결과(-28)

