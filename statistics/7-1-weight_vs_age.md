[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```
from __future__ import print_function, division

%matplotlib inline

import numpy as np
import pandas as pd

import brfss

import thinkstats2
import thinkplot
import first

live, firsts, others = first.MakeFrames()
live = live.dropna(subset = ['agepreg', 'totalwgt_lb'])

age = live.agepreg
weight = live.totalwgt_lb

def ScatterPlot(age, weight, alpha=1.0):
    thinkplot.Scatter(age, weight)
    thinkplot.Config(xlabel='Age (years)',
                     ylabel='Birth weight (pounds)',
                     axis = [10, 45, 0, 15])
    
ScatterPlot(ages, weights, alpha=0.05)

def Covariance(xs, ys, meanx=None, meany=None):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    if meanx is None:
        meanx = np.mean(xs)
    if meany is None:
        meany = np.mean(ys)

    covariance = np.dot(xs-meanx, ys-meany) / len(xs)
    return covariance

def Correlation(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    meanx, varx = thinkstats2.MeanVar(xs)
    meany, vary = thinkstats2.MeanVar(ys)

    correlation = Covariance(xs, ys, meanx, meany) / np.sqrt(varx * vary)
    return correlation
    
def Spearman_Correlation(xs, ys):
    xranks = pd.Series(xs).rank()
    yranks = pd.Series(ys).rank()
    return Correlation(xranks, yranks)
    
print('Pearson Correlation:', Correlation(ages, weights))
print('Spearman Correlation:', Spearman_Correlation(ages, weights))

```
