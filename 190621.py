import torch
import torch.nn as nn

# data, model. output update

# X and Y data

#torch, tensor([1,2,3]),float()
#.float()
x_train = torch.tensor([[1],[2],[3],[4]]).float()
y_train = torch.tensor([[0],[0],[1],[1]]).float()

#Model H(x) = Wx + b
class LogisticModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LogisticModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)
    def forward(self,x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

model = LogisticModel(1,1)
cost = nn.BCELoss()
cost=nn.MSELoss()
optim=torch.optim.SGD(model.parameters(),lr=0.001)

#our hypothesis
for epoch in range(10000):
    diff = model(x_train)
   # print("diff value", diff)
    optim.zero_grad()
    output = model.forward(x_train)
    loss = cost(output,y_train)
    loss.backward()
    optim.step()
    print(loss)