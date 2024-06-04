import numpy as np

def MD_nRE(y, y_hat, n=2, p=1):

    return (np.abs(np.power(y, 1/n) - np.power(y_hat, 1/n))) ** p

# Example usage
y = [100, 50, 20, 5.5, 1.0, 0.6]
y_hat = [ 99.5, 49.5, 19.5, 5.0, 0.5, 0.1]
p = 1
n = 2

for i in range (0,len(y)):
    result = MD_nRE(y[i], y_hat[i], n, p)
    print(f"MD_nRE: {result}")