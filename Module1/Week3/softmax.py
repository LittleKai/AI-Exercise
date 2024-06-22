import torch

class Softmax(torch.nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x

class SoftmaxStable(torch.nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / (sum_exp_x + 1e-12)

data = torch.Tensor([1, 2, 3])

softmax = Softmax()
output = softmax(data)
print(output)

softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
print(output_stable)