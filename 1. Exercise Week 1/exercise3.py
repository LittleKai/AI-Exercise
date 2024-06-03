import numpy as np
import random

def exercise3():
    n = input("Input number of samples ( integer number ) which are generated : ")

    if not n.isnumeric():
        print("The number of samples must be an integer")
        return

    n = int(n)
    loss_function = input("Input loss name (MAE|MSE|RMSE): ")
    if loss_function not in ["MAE", "MSE", "RMSE"]:
        print(f"'{loss_function}' is not supported")
        return
    final_loss = 0
    for i in range(0, n):
        pred_value = random.uniform(0, 10)
        target_value = random.uniform(0, 10)
        loss = calculate_metrics(loss_function, pred_value, target_value)
        final_loss = final_loss + loss
        print(f'loss name : {loss_function} , sample : {i} , pred : {pred_value}, target : {target_value}, loss : {loss}')
    
    if loss_function == "RMSE":
        final_loss = final_loss/np.sqrt(n)
    else:
        final_loss = final_loss/n
    print(f'final {loss_function}: {final_loss}')

def calculate_metrics(loss_name, pred_value, target_value):
    if loss_name == "MAE":
        result = np.abs(pred_value - target_value)
    elif loss_name == "MSE":
        result = (pred_value - target_value) ** 2
    else:
        result = np.sqrt((pred_value - target_value) ** 2)

    return result

exercise3()