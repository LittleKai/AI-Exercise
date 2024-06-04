import numpy as np

def exercise2():

    x = input("Input x: ")
    try:
        x = float(x)
    except ValueError:
        print("x must be a number")
        return

    activation_function = input("Input activation Function (sigmoid|relu|elu): ")
    if activation_function not in ["sigmoid", "relu", "elu"]:
        print(f"'{activation_function}' is not supported")
        return

    if activation_function == "sigmoid":
        output = sigmoid(x)
    elif activation_function == "relu":
        output = relu(x)
    else:
        output = elu(x)


    print(f"Input: {x}")
    print(f"Activation Function: {activation_function}")
    print(f"{activation_function}: f({x}) =  {output}")

# Hàm sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Hàm relu
def relu(x):
    return np.maximum(0, x)

# Hàm elu
def elu(x):
    if x >= 0:
        return x
    else:
        return 0.01 * (np.exp(x) - 1)

exercise2()