[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
from __future__ import print_function, division
%matplotlib inline
import numpy as np
import nsfg
import first
import analytic
import thinkstats2
import thinkplot

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
# A: scipy.stats._distn_infrastructure.rv_frozen

dist.mean(), dist.std()
# A: (178.0, 7.7000000000000002)

dist.cdf(mu-sigma)
# A: 0.15865525393145741

low = dist.cdf(177.8)
high = dist.cdf(185.42)
low, high, high-low
# A: (0.48963902786483265, 0.83238586549630633, 0.34274683763147368)

(high-low) * 100
# A: 34.27% of the U.S. population falls within this range.
```
