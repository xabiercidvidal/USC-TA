# Introduction

Author: José Ángel Hernando Morata, Xabier Cid Vidal

Institution: Physics Master, **Universidade de Santiago de Compostela**

email: jose.hernando@usc.es, [xabier.cid@usc.gal](mailto:xabier.cid@usc.gal)

Version: February 2025


## About these lectures

These lectures are about statistical methods for rare event searches in Particle Physics using Python. 

They cover Hypothesis Testing and Confidence Level Intervals. They are based on the excellent lectures on statistics by Prosper ([lectures](https://indico.cern.ch/event/358542) [pdf](https://arxiv.org/pdf/1504.00945.pdf)), Cowan ([lectures](http://indico.cern.ch/event/173726/)) and Cranmer ([lectures](https://indico.cern.ch/event/48425/)) given at the CERN Academic Training.

Sometimes, we do an experiment to discover a new particle. If the particle exists in Nature we may only find few events. 
Rare events usually follow poissonian distributions, but statistics are nicely and friendly in the "Gaussian domain".

When could we clain that we have an **observation** or a **discovery** of the new particle? 
And if not, what is the **limit** on a given observable (i.e. the half lifetime) that we could impose?

In fact, *what does it mean discovery, observation, a limit, a confidence level interval?* and, *how do we compute them from data?* These are the questions we try to answer in these lectures.

The beginning starts with a bifurcation: either we follow a **Bayes** or a **Frequentist** path.
Being a Bayesian implies doing **integration** (sometime complicated integrals!), and being a frequentist implies either doing regressions (fits!) or **simulations**.  But thanks to the current computing power, we can play the **frequentist game**!

We will use Python scientific toolkits, Matplotlib, Numpy, Scipy, that are distributed with Anaconda Python. 

## Table of Contents

```{tableofcontents}
```

## Bibliography

[1] "Practical Statistic for LHC physicist," H. B. Prosper, CERN Academic Training Lectures (2015). [Lectures](https://indico.cern.ch/event/358542/) [PDF](https://arxiv.org/pdf/1504.00945.pdf)

[2] "Statistic for HEP," G. Cowan. CERN Academic Training Lectures (2012). [Lectures](http://indico.cern.ch/event/173726/)

[3] "Statistics for Particle Physics," K. Cranmer, CERN Academic Training Lectures (2009). [Lectures](https://indico.cern.ch/event/48425/)

[4] "Unified approach to the classical statistical analysis of small signals, "G. J. Feldman and R. D. Cousins, [Phys. Rev. D57 (1998) 3873.])(http://journals.aps.org/prd/abstract/10.1103/PhysRevD.57.3873)

[5] “Asymptotic formulae for likelihood-based tests of new physics,” Glen Cowan, Kyle Cranmer, Eilam Gross, Ofer Vitells. [Eur. Phys. J. C71 1554 (2011).](https://arxiv.org/abs/1007.1727)

[6] "Incorporating systematic uncertainties into an upper limit," R.D. Cousins and V.L. Highland. [Nucl. Instrum. Meth. A320, 331 (1992).](http://www.sciencedirect.com/science/article/pii/0168900292907945)

[7] "Confidence Level Computation for Combining Searches with Small Statistics," T. Junk, [Nucl. Instrum. Meth. A434, 435 (1999).](https://arxiv.org/abs/hep-ex/9902006)

[8] "How good are your fits? Unbinned multivariate goodness-of-fit tests in high energy physics," M. Willians, [ArXiv:1006.3019](https://arxiv.org/abs/1006.3019)

[9] [ROOT](https://root.cern.ch), [TMVA](http://tmva.sourceforge.net), [RooFit](https://root.cern.ch/roofit)

[10] [Anaconda](https://anaconda.org), 

[11] "Lectures on Statistics in Theory: Prelude to Statistics in Practice" B. Cousins, [ArXiv:1807.05006](https://arxiv.org/abs/1807.05996)

[12] "Statistics for physics". D. Tonelli. Invisible School 2019, Canfranc.

[13] The Monty Hall Problem Using Bayes’ Theorem https://blogs.cornell.edu/info2040/2022/11/10/the-monty-hall-problem-using-bayes-theorem/
