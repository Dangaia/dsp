[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```
resp = nsfg.ReadFemResp()

pmf_numkdhh = thinkstats2.Pmf(resp.numkdhh, label = 'numkdhh')

thinkplot.Pmf(pmf_numkdhh)
thinkplot.Config(xlabel = 'Number of Children in Household', ylabel = 'PMF') 

biased_numkdhh = BiasPmf(pmf, label = 'biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_numkdhh, biased_numkdhh])
thinkplot.Show(xlabel='Number of Children in Household', ylabel='PMF')

pmf_numkdhh.Mean()
1.0242051550438309

biased_numkdhh.Mean()
2.4036791006642821
```
