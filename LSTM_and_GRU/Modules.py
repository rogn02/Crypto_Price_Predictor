from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
import math,time,torch
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pickle
#initailizing common parameters for LSTM and GRU
input_dim = 1
hidden_dim = 10
num_layers =1
output_dim = 1
num_epochs = 500
