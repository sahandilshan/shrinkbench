"""Small CNN designed for MNIST, intended for debugging purposes

[description]
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from . import weights_path


class MnistNet(nn.Module):
    """Small network designed for Mnist debugging
    """
    def __init__(self, pretrained=False):
        super(MnistNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5, 1)
        self.conv2 = nn.Conv2d(20, 50, 5, 1)
        self.fc1 = nn.Linear(4*4*50, 500)
        self.fc2 = nn.Linear(500, 10)
        self.fc2.is_classifier = True
        if pretrained:
            weights = weights_path('mnistnet.pt')
            self.load_state_dict(torch.load(weights))

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 4*4*50)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
