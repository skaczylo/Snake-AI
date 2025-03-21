import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
from collections import deque
import torch.nn.functional as F

class DQN(nn.Module):

    def __init__(self,state_dim,action_dim):
        super().__init__()
        self.fc1 = nn.Linear(state_dim, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, action_dim)
    
    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
    def save(self,path):
        torch.save(self.state_dict(), path)






