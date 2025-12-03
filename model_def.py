import torch.nn as nn

class clsModel(nn.Module):
    def __init__(self):
        super(clsModel, self).__init__()
        
        layers = []
        
        # Input layers
        layers.append(nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1))
        layers.append(nn.BatchNorm2d(32))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.MaxPool2d(kernel_size=2, stride=2))  # -> (32, 14, 14)

        layers.append(nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1))
        layers.append(nn.BatchNorm2d(64))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.MaxPool2d(kernel_size=2, stride=2))  # -> (64, 7, 7)

        layers.append(nn.Flatten())  # -> (64*7*7,)
        layers.append(nn.Linear(in_features=64*7*7, out_features=128))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.Linear(in_features=128, out_features=10))
        
        self.model = nn.Sequential(*layers)
    
    def forward(self,x):
        return self.model(x)
        
        
        