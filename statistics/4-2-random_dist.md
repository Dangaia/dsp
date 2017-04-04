[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
from __future__ import print_function, division
%matplotlib inline
import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

random_1000 = np.random.random(1000)

random_1000_pmf = thinkstats2.Pmf(random_1000)
thinkplot.Pmf(random_1000_pmf, linewidth = 0.1)
thinkplot.Config(xlabel = 'Random Number', ylabel = 'PMF') 
# Q: What goes wrong?
# A: The graph looks just like vertical stripes because each number has the same probabilty. 

random_1000_cdf = thinkstats2.Cdf(random_1000)
thinkplot.Cdf(random_1000_cdf)
thinkplot.Config(xlabel= 'Random Number', ylabel = 'CDF')
# Q: Is the distribution uniform?
# A: Yes.
```
