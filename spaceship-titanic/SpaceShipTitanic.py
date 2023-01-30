# author Eleanor Watson
# date 30-01-2023

# Filepath
fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Kubrick\\ML_work\\kaggle\\spaceship_titanic_kaggle\\spaceship-titanic\\"
# imports 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

## File read 

train_fp = fp + "train.csv"

df = pd.read_csv(train_fp)

## Exploratory Data Analysis

fig, ax = plt.subplots()
ax.scatter(df['Age'], df['Transported'])
ax.grid()
ax.plot()


print("----------------")
