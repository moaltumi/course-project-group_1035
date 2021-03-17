{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

#line 22

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#line 30
#changed by aneeq
def load_and_process(url_or_path_to_csv_file):
    
    df = (pd.read_csv(url_or_path_to_csv_file)
          .drop(columns = ['DIVERTED','CANCELLED', 'CANCELLATION_REASON', 'AIR_SYSTEM_DELAY', 'SECURITY_DELAY','AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY','WEATHER_DELAY'])
          .dropna(axis = 1)
          .rename(columns = {"WHEELS_OFF" : "GATE_TO_TAKEOFF"}))
    return df


def displot(df,df_col,plot_title): # put col name as string in df_col, title as string in plot_title, and bins as integer keep it default
    sns.distplot(df[df_col], kde=False).set_title(plot_title)

    
    
    
def barplot(df,colx,coly,plot_title):
    sns.barplot(x = colx, y = coly, data = df).set_title(plot_title)
    
    
def correlmatrix(df): #method to plot correlation matrix, it show relation between all attributes
    corr = df.corr()# plot the heatmap
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns,linewidths=0.5, vmin=0, vmax=1, annot=False, annot_kws={"size":8},cmap=sns.diverging_palette(200, 20, as_cmap=True))
        
        
        
def scatterPlot(df,colx,coly): # to plot scatterplot shows relation between any two attributes
    df.plot(kind='scatter', x=colx, y=coly)    
    
def countPlot(df,col):
    sns.countplot(x=col, data=df)

#your previous code dosen't work
# def load_and_process(url_or_path_to_csv_file):
    
    
#     df = (pd.read_csv(url_or_path_to_csv_file)
#           .drop(columns = ['DIVERTED','CANCELLED', 'CANCELLATION_REASON', 'AIR_SYSTEM_DELAY', 'SECURITY_DELAY','AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY','WEATHER_DELAY','Unamed: 31'])
#           .dropna(axis = 0)
#           .rename(columns = {"WHEELS_OFF" : "GATE_TO_TAKEOFF"}))
#     return df



    
    #don't need these just call the above function with your requirements
# def displot2(df):
#     sns.displot(df['AIRLINE'], kde=False, bins=13).set_title('amount of flights per airline')
    
    
# def displot3(df):
#     sns.displot(df['ORIGIN_AIRPORT'], kde=False, bins=322).set_title('departing flights')
    
    
# def barplot(df):
#     sns.barplot(y = 'DELAYED_OR_NOT', data =df).set_title('number of flights delayed versus on time')



