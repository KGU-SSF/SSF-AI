import numpy as np

input_data=5                            #입력값
weight=3                                #가중치
target=8                                #실제값
learning_rate=0.1                       #학습률
pred=weight*input_data                  #예측값 = 입력값 x 가중치

error=pred-target                       #오차 = 예측값 - 실제값 (순서 바뀌어도 상관x <- 어차피 제곱할 것)
print("original error:",error)          #5x3-8=7

slope=2*input_data*error                #기울기 = 2 x 입력값 x 오차
print("slope:",slope)                   #2x5x7=70

new_weight=weight-learning_rate*slope   #새로운 가중치 = 가중치 - 학습률(기울기 보폭) x 기울기 <경사 하강법>
print("new weight:",new_weight)         #3-0.1x70=-4

new_pred=new_weight*input_data          #새로운 예측값 = 새로운 가중치 x 입력값
print("new prediction:",new_pred)       #-4x5=-20

new_error=new_pred-target               #새로운 오차 = 새로운 예측값 - 실제값
print("new error:",new_error)           #-20-8=-28