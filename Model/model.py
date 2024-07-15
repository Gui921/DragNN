import torch
from torch import nn

class NeuralNetwork(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.layers_block = nn.ModuleList()
        
    def forward(self, x):
        for layer in self.layers_block:
            x = layer(x)
        
        return x
    
    def add_dense_layer(self, out_features):
        layer = nn.Linear(self.in_channels, out_features)
        self.layers_block.append(layer)
        self.in_channels = out_features

    def add_conv_layer_2d(self, out_channels, kernel_size, stride=1, padding=0):
        layer = nn.Conv2d(self.in_channels, out_channels, kernel_size, stride, padding)
        self.layers_block.append(layer)
        self.in_channels = out_channels 

    def add_conv_layer_3d(self, out_channels, kernel_size, stride=1, padding=0):
        layer = nn.Conv3d(self.in_channels, out_channels, kernel_size, stride, padding)
        self.layers_block.append(layer)
        self.in_channels = out_channels
    
    def add_transposed_conv_layer_2d(self, out_channels, kernel_size, stride=1, padding=0):
        layer = nn.ConvTranspose2d(self.in_channels, out_channels, kernel_size, stride, padding)
        self.layers_block.append(layer)
        self.in_channels = out_channels
    
    def add_transposed_conv_layer_3d(self, out_channels, kernel_size, stride=1, padding=0):
        layer = nn.ConvTranspose3d(self.in_channels, out_channels, kernel_size, stride, padding)
        self.layers_block.append(layer)
        self.in_channels = out_channels 
    
    def add_activation_layer(self, activation_function='ReLu'):
        if activation_function == 'Sigmoid':
            self.layers_block.append(nn.Sigmoid())
        elif activation_function == 'Tanh':
            self.layers_block.append(nn.Tanh())
        elif activation_function == 'Leaky ReLu':
            self.layers_block.append(nn.LeakyReLU())
        elif activation_function == 'Softmax':
            self.layers_block.append(nn.Softmax())
        else:
            self.layers_block.append(nn.ReLU())
    
    def add_maxpool_layer_2d(self, kernel_size, stride=None, padding=0):
        layer = nn.MaxPool2d(kernel_size, stride, padding)
        self.layers_block.append(layer)
    
    def add_averagepool_layer_2d(self,kernel_size,stride=None,padding=0):
        layer = nn.AvgPool2d(kernel_size,stride,padding)
        self.layers_block.append(layer)

    def add_maxpool_layer_3d(self, kernel_size, stride=None, padding=0):
        layer = nn.MaxPool3d(kernel_size, stride, padding)
        self.layers_block.append(layer)
    
    def add_averagepool_layer_3d(self,kernel_size,stride=None,padding=0):
        layer = nn.AvgPool3d(kernel_size,stride,padding)
        self.layers_block.append(layer)

    def add_flatten_layer(self):
        self.layers_block.append(nn.Flatten())
    
    def add_dropout_layer(self, p=0.5):
        self.layers_block.append(nn.Dropout(p))

    def add_dropout_layer_2d(self, p=0.5):
        self.layers_block.append(nn.Dropout2d(p))
    
    def add_dropout_layer_3d(self, p=0.5):
        self.layers_block.append(nn.Dropout3d(p))

    def add_batchnorm_layer_2d(self, num_features):
        layer = nn.BatchNorm2d(num_features)
        self.layers_block.append(layer)

    def add_batchnorm_layer_3d(self, num_features):
        layer = nn.BatchNorm3d(num_features)
        self.layers_block.append(layer)


# TEST

#model = NeuralNetwork(15, 2)
#model.add_dense_layer(5)
#model.add_dense_layer(2)

#print(model)


