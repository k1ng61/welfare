import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset



train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

trainset = torch.utils.data.DataLoader(train_df, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test_df, batch_size=10, shuffle=True)


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(36, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 16)
        self.fc4 = nn.Linear(16, 3)
        self.fc5 = nn.Linear(3, 20)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)

        return F.log_softmax(x, dim=1)

net = Net()

optimizer = optim.Adam(net.parameters(), lr=0.001)
EPOCHS = 3

for epoch in range(EPOCHS):
    for data in trainset:
        x, y = data
        net.zero_grad()
        output = net(x.view(-1, 28 * 28))
        loss = F.nll_loss(output, y)
        loss.backward()
        optimizer.step()

correct = 0
total = 0

with torch.no_grad():
    for data in trainset:
        x, y = data
        output = net(x.view(-1, 784))
        for idx, i in enumerate(output):
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1

print(round(correct / total, 3))

