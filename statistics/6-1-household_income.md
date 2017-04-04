[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

```
from __future__ import print_function, division

%matplotlib inline

import numpy as np
import thinkstats2
import thinkplot


def InterpolateSample(df, log_upper=6.0):
    df['log_upper'] = np.log10(df.income)
    df['log_lower'] = df.log_upper.shift(1)
    df.loc[0, 'log_lower'] = 3.0
    df.loc[41, 'log_upper'] = log_upper
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)
    log_sample = np.concatenate(arrays)
    return log_sample

import hinc
income_df = hinc.ReadData()

log_sample = InterpolateSample(income_df, log_upper=6.0)

log_cdf = thinkstats2.Cdf(log_sample)
thinkplot.Cdf(log_cdf)
thinkplot.Config(xlabel='Household income (log $)', ylabel='CDF')

sample = np.power(10, log_sample)

cdf = thinkstats2.Cdf(sample)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Household income ($)', ylabel='CDF')

def Mean(xs):
    return RawMoment(xs, 1)
    
def Median(xs):
    cdf = thinkstats2.Cdf(xs)
    return cdf.Value(0.5)
    
def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)
    
def StandardizedMoment(xs, k):
    var = CentralMoment(xs, 2)
    std = np.sqrt(var)
    return CentralMoment(xs, k) / std**k

def Skewness(xs):
    return StandardizedMoment(xs, 3)
    
def PearsonMedianSkewness(xs):
    median = Median(xs)
    mean = RawMoment(xs, 1)
    var = CentralMoment(xs, 2)
    std = np.sqrt(var)
    gp = 3 * (mean - median) / std
    return gp
    
Mean(sample)
# A: 74278.707531187334

Median(sample)
# A: 51226.454478940461

Skewness(sample)
# A: 4.9499202444295829

PearsonMedianSkewness(sample)
# A: 0.7361258019141782

# What fraction of households reports a taxable income below the mean?
(cdf.Prob(Mean(sample))) * 100
# A: 66.000587956687198
# A: About 66% of households report a taxable income below the mean.
```

          
