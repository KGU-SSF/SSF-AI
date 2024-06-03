input_data = np.array([[3, 5], [1, -1], [0, 0], [8, 4]])
weight = np.array([[2], [7]])
target = np.array([[33], [-5], [0], [31]])
learning_rate = 0.001

def predict(X, W):
    return X.dot(W)
def gradient(X, error):
    return 2 * X.T.dot(error)
def update(W, gd, learning_rate):
    W= W - learning_rate * gd 
    return W
def cost(error):
    return (error**2).mean()
epoch = 20

for i in range(epoch):
    pred = predict(input_data, weight)
    error = pred - target
    print(f"cost at epoch {i}: {cost(error[0]):.4f}")
    gd = gradient (input_data, error)
    weight = update(weight, gd, learning_rate)
print('final prediction:', predict(input_data, weight))