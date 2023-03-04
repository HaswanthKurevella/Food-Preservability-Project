# IMPORTING MODULES
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# DATA HANDLING
data = pd.read_csv('preserve.csv')
print(data.head())
print(data.describe())
X = data[['NATURAL_FACTORS', 'INFESTATION_CONTROL', 'SHIPPING', 'LOCATION_HISTORY', 'WORK_FORCE', 'STORAGE', 'FINANCE']]
Y = data['PRESERVE_FACTOR']
Y_ = data['EFFICIENCY']

# DATA ANALYSIS
plt.scatter(X['NATURAL_FACTORS'], Y, color='b')
plt.xlabel('NATURAL_FACTORS')
plt.ylabel('PRESERVE_FACTOR')
plt.show()
