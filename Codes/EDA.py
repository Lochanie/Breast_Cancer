# Explanatory Data Analysis for Breast_Cancer Data - to get an idea about the dataset
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport



cancer_data =pd.read_csv('/home/lochanie/Documents/Breast_Cancer/raw_data/Breast_Cancer.csv')
# print(cancer_data.head(10))

# Get all column names
#print(cancer_data.dtypes)

#Get the informative statistics of data set
#cancer_data.info()

#get the descriptive statistics of dataset
#print(cancer_data.describe())
#cancer_data.describe().to_csv("descriptive Statistics.csv")

#****************************************************************
#Explaonatory Data Analysis

#heat map of data distribution
# ax = sns.heatmap(cancer_data, vmin=10, vmax=40,cmap='tab20')
# plt.title('Heat Map Between Selected Parameters')
# plt.show()

# corr = cancer_data.corr()
# ax1 = sns.heatmap(corr, cbar=0, linewidths=2,vmax=1, vmin=0, square=True, cmap='Blues')
# plt.title('Heat Map Between Selected Parameters')
# plt.show()


#Data set Profile

report = ProfileReport(cancer_data, title="Cancer data pandas profile report")
report.to_notebook_iframe()









