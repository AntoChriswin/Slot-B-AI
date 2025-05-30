mport numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.5):
        # Weights initialization
        self.learning_rate = learning_rate
        self.input_size = input_size

        # Weights between input layer and hidden layer
        self.weights_input_hidden = np.random.uniform(-1, 1, (input_size, hidden_size))
        # Bias for hidden layer
        self.bias_hidden = np.random.uniform(-1, 1, (1, hidden_size))

        # Weights between hidden layer and output layer
        self.weights_hidden_output = np.random.uniform(-1, 1, (hidden_size, output_size))
        # Bias for output layer
        self.bias_output = np.random.uniform(-1, 1, (1, output_size))

    def forward(self, X):
        # Input to hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)

        # Hidden to output layer
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)

        return self.final_output

    def backward(self, X, y, output):
        # Calculate output error
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        # Calculate hidden layer error
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)

        # Update weights and biases
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * self.learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate

        self.weights_input_hidden += X.T.dot(hidden_delta) * self.learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}, Loss: {loss:.6f}")

    def predict(self, X):
        output = self.forward(X)
        return (output > 0.5).astype(int)

if __name__ == "__main__":
    # Training dataset for AND logic gate
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([
        [0],
        [0],
        [0],
        [1]
    ])

    # Initialize neural network: 2 inputs, 2 hidden neurons, 1 output
    nn = FeedforwardNeuralNetwork(input_size=2, hidden_size=2, output_size=1, learning_rate=0.5)

    # Train the network
    nn.train(X, y, epochs=10000)

    # Test predictions
    print("\nTesting predictions:")
    for x_input, label in zip(X, y):
        pred = nn.predict(x_input.reshape(1, -1))
        print(f"Input: {x_input}, Predicted: {pred[0][0]}, Actual: {label[0]}")
