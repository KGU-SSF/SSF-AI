input_data=5 #입력값
weight=3 #가중치
target=8 #목표값
learning_rate=0.1 #학습률
pred=weight*input_data #예측값(3*5=15)

error=pred-target #오차(15-8=7)
print("original error",error) #결과출력(7)

slope=2*input_data*error #기울기(2*5*7=70)
print('slope:',slope) #결과출력(70)

new_weight=weight-learning_rate*slope #새 가중치(3-0.1*70=-4)
print('new weight:',new_weight) #결과출력(-4.0)

new_pred=new_weight*input_data #새 예측값(-4*5=-20)
print('new prediction:',new_pred) #결과출력(-20.0)

new_error=new_pred-target #새 오차(-20-8=-28)
print('new error:',new_error) #결과출력(-28.0)