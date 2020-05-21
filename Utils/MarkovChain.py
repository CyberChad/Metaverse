#Import gym and this package:

import gym
#import sc2gym.envs

#Import and initialize absl.flags: (this is due to pysc2 dependency)

import sys
from absl import flags
FLAGS = flags.FLAGS
FLAGS(sys.argv)

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

#print(pd.__version__)

#my_series = pd.Series([4.6, 2.1, -4.0, 3.0])
#print(my_series.values)

#import csv
#exampleFile = open("D:\OneDrive - Carleton University\SC2-Replays-64k-colfilter.csv")
#exampleDictReader = csv.DictReader(exampleFile)

#***************** Data Frames ************************

df  = pd.read_csv("D:\OneDrive - Carleton University\SC2-Replays-64k-colfilter.csv")
print(df.head(5))
#print(dataframe.tail(2))
#print(dataframe['Avg APM'])
#print(dataframe['Avg APM'][0])
print(df.shape)

filterAPM = df['AvgAPM']<=800
#print(filterAPM.head())
df2 = df[filterAPM]

print(df2.shape)

filterSPM = df2['AvgSPM']<=150
df3 = df2[filterSPM]

print(df3.shape)

flier_high = 1400
flier_low = 0

x = df3.AvgSPM
y = df3.AvgAPM

plt.scatter(x,y)
plt.xlabel('Avg Screens per Minute')
plt.ylabel('Avg Actions per Minute')
#plt.show()

npvals = df3.values

np_r = np.corrcoef(x,y)
print("Numpy corrcoeff: %5f " % np_r[0,1])

scipy_r = stats.pearsonr(x, y)[0]

print("Scipy corrcoeff: %5f " % scipy_r)

#bootstrap = pd.plotting.bootstrap_plot(x)

sns.set(color_codes=True)
x = np.random.normal(size=100)
sns.distplot(x)
plt.show()



