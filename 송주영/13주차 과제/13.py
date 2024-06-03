import numpy as np

input_data=np.array([[3,5],[1,-1],[0,0],[8,4]])
weight=np.array([[2],[7]])
target=np.array([[33],[-5],[0],[31]])
learning_rate=0.001
bias = 0

def predict(X,W, b):
    return X.dot(W) + b

def gradient(X, error):
    return 2*X.T.dot(error), np.sum(error)

def update(W,b,gd,learning_rate):
    W=W-learning_rate*gd[0]
    b = b-learning_rate*gd[1]
    return W,b

def cost(error):
    return(error**2).mean()

epoch=20

for i in range(epoch):
    pred=predict(input_data, weight, bias)
    error=pred-target
    print(f"cost at epoch{i}: {cost(error[0]):.4f}")
    gd=gradient(input_data,error)
    weight, bias=update(weight,bias, gd,learning_rate)
print('final predinction:',predict(input_data,weight,bias))