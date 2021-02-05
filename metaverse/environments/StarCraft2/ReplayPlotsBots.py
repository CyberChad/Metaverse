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

#***************** Data Frames ************************


def df_import(file):

    df = pd.read_csv(file)
    print(df.head(5))
    #print(dataframe.tail(2))
    #print(dataframe['Avg APM'])
    #print(dataframe['Avg APM'][0])
    print(df.shape)

    return df

def df_correlation(df):


    x = df.APM1
    y = df.ELO

    #npvals = df.values

    np_r = np.corrcoef(x,y)
    print("Numpy corrcoeff: %5f " % np_r[0,1])

    scipy_r = stats.pearsonr(x, y)[0]
    print("Scipy corrcoeff: %5f " % scipy_r)


def df_filter(df):

    filterAPM = df['AvgAPM']<=800
    #print(filterAPM.head())
    df2 = df[filterAPM]
    print(df2.shape)

    filterSPM = df2['AvgSPM']<=150
    df3 = df2[filterSPM]
    print(df3.shape)

    return df3

def df_scatterplot(df):
    flier_high = 1400
    flier_low = 0

    y = df.APM1
    x = df.ELO

    plt.scatter(x,y)
    plt.ylabel('Avg Actions per Minute')
    plt.xlabel('ELO Rating')
    plt.show()

    #npvals = df.values

    np_r = np.corrcoef(x,y)
    print("Numpy corrcoeff: %5f " % np_r[0,1])

    scipy_r = stats.pearsonr(x, y)[0]

    print("Scipy corrcoeff: %5f " % scipy_r)

    #bootstrap = pd.plotting.bootstrap_plot(x)

    #sns.set(color_codes=True)
    #x = np.random.normal(size=100)
    #sns.distplot(x)

    #ax = sns.scatterplot(x="APM1",y="ELO",data=df)
    #plt.show()

def df_boxplot(df):
    # create collections per league
    print(df.shape)

    #ax = sns.boxplot(x=df["APM1"])

    Q0 = df['APM1'].quantile(0.05)
    Q1 = df['APM1'].quantile(0.25)
    Q3 = df['APM1'].quantile(0.75)
    IQR = Q3-Q1
    lower = Q1-1.5*IQR
    upper = Q3+1.5*IQR

    print("Q0: " + str(Q0))
    print("Q1: "+str(Q1))
    print("Q3: "+str(Q3))
    print("IQR: "+str(IQR))
    print("lower: " + str(lower))
    print("upper: "+str(upper))

    #plt.show()

    filter = df['APM1'] <= upper

    dfFiltered = df[filter]
    print(dfFiltered.shape)
    df=dfFiltered

    Q0 = df['APM1'].quantile(0.05)
    Q1 = df['APM1'].quantile(0.25)
    Q3 = df['APM1'].quantile(0.75)
    IQR = Q3-Q1
    lower = Q1-1.5*IQR
    upper = Q3+1.5*IQR

    dfarray = df['APM1']
    mean = dfarray.values.mean()
    print("mean: " + str(mean))
    std = dfarray.values.std(ddof=1)
    print("std: "+str(std))

    print("Q0: " + str(Q0))
    print("Q1: "+str(Q1))
    print("Q3: "+str(Q3))
    print("IQR: "+str(IQR))
    print("lower: " + str(lower))
    print("upper: "+str(upper))

    #dfAPMbyLeague = pd.DataFrame(dfBronze.APM1)
    #print(dfAPMbyLeague.shape)
    #print(dfAPMbyLeague.head(5))

    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    # bp = ax.boxplot(by=dfAPMbyLeague)
    # plt = df.boxplot(column=['APM1'])

    # sns.set(color_codes=True)
    sns.set(style="whitegrid")
    # apms = sns.load_dataset()
    ax = sns.boxplot(x=df["ELO"], y=df["APM1"])
    #ax = sns.boxplot(x=df["APM1"])
    plt.show()

def df_heatmap(df3):
    # Compute the correlation matrix
    corr = df3.corr()
    print(corr)
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 11))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, linewidths=0.1, square=True, cbar_kws={"shrink": .75})
    plt.show()

def plotbyleague():
    file1 = "D:\OneDrive - Carleton University\StarCraft 2 Dataset Analysis\SC2-Replays-64k-colfilter2.csv"
    df1 = df_import(file)
    df2 = df_filter(df1)
    #df_scatterplot(df2)
    #df_boxplot(df2)
    df_heatmap(df2)


if __name__ == "__main__":

    file = "D:\OneDrive - Carleton University\Development\\sc2ai_ladder8_apm_elo_fixed.csv"


    df = df_import(file)

    df_correlation(df)

    #df_scatterplot(df)

    #df_boxplot(df)




