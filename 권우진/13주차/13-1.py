# import numpy as np

# # 선형 회귀

# input_data = np.array([[3 ,5], [1, -1], [0, 0], [8, 4]])
# weight = np.array([[2], [7]])
# target = np.array([[33], [-5], [0], [31]])
# learning_rate = 0.001
# bias = 0

# def predict(X, W, b):
#     return X.dot(W) + b

# def gradient(X, error):
#     return 2 * X.T.dot(error), np.sum(error)

# def update(W, b, gd, learning_rate):
#     W = W - learning_rate * gd[0]
#     b = b - learning_rate * gd[1]
#     return W, b

# def cost(error):
#     return (error**2).mean()

# epoch = 20

# for i in range(epoch):
#     pred = predict(input_data, weight, bias)
#     error = pred - target
#     print(f"cost at epoch {i}: {cost(error[0]):.4f}")
#     gd = gradient(input_data, error)
#     weight, bias = update(weight, bias, gd, learning_rate)
# print("final prediction: ", predict(input_data, weight, bias))

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

diabetes = load_diabetes()
X_data = diabetes.data
y_data = diabetes.target

x_train, x_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(x_train, y_train)

y_train_pred = lr.predict(x_train)
r2_train = r2_score(y_train, y_train_pred)
print(f"r2_train: {r2_train}")
y_test_pred = lr.predict(x_test)
r2_test = r2_score(y_test, y_test_pred)
print(f"r2_test: {r2_test}")