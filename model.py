import torch.nn as nn

class ModelFeux(nn.Module):
    def __init__(self):
        super(ModelFeux, self).__init__()
        self.fc = nn.Linear(2, 2)

    def forward(self, x):
        return self.fc(x)