### Exercises
**Do the following exercises.**
#### Exercises 1: Hypothesis testing (simple case)

##### Exercise 1a: 
Consider the NEXT experiment as a counting experiment. 
- Compute the number of possible $\beta{\beta}0\nu$ events in 100 kg of Xenon if the half-lifetime is $10^{-25}$ y. 
- Compute also the number of expected background events, if the background index is $4 \times 10^{-4}$ counts/(keV kg y) and with 1% energy resolution at $Q_{\beta\beta} = 2.458$ MeV. 
- Obtain the pdfs of the test statistics. Consider that the signal is gaussian distributed and take 3 sigmas as Region of Interest (RoI).
- Now modify the background index, the resolution, the Xe mass and the half-lifetime.

##### Exercise 1b:
Consider the expected background events and signal events in bins of energy in the RoI of the KamLAND-Zen experiment in Fig 2-b) [PRL-117](https://arxiv.org/abs/1605.02889). 
- Compute now the pdfs of $q$ for only background and 10 times the signal.
- Compute the p-value of $H_0$.

##### Exercise 1c:
An experiment expects $(2, 1)$ background events in two bins, and a possible signal $(8, 9)$ on top. 
- It observes $(9, 9)$, can we claim an observation?
- In case it observes $(1, 1)$, can reject the signal at 95 % CL?

##### Exercise 1d:
Consider now an experiment with several independent channels that expects as background ${\bf b} = (2, 1.5, 1, 0.5)$ and as signal ${\bf s} = (1, 3, 3, 1)$. It measures $(2, 1, 1, 0)$. Compute the p-value of $H_1$.

#### Exercises 2: Confidence intervals

**Prepare a total of 3 exercises.**

##### Exercise 2a: 
Construct the *confidence belt* CI at 90% and 68% CL considering a counting experiment with background $b$ and unknown signal $\mu$. In this case, the pdf is a poisson with mean $b + \mu$. We scan along $\mu$ and for each $\mu$ we obtain the interval $[x_l(\mu), x_u(\mu)]$ using the central interval at 90% contaiment. Then, we unify the border of the segments and we define the confident belt.
- What is the CI at 90% CL? And for $b=3$ and $x_0 = 1$?
- Test the coverage of the CI at 90% CL in this example. Consider $b=2$ and $\mu_{true} = 2$.

**Choose at least 2 among the exercises 2b, 2c and 2d:**

##### Exercise 2b:
Verify that the flip-flop problem has not the proper coverage.

##### Exercise 2c: 
FC is a frequentist method. Verify now that the FC contruction guarantees **coverage** for some examples $b = 3, \mu_{true} = 0.5$

##### Exercise 2d: 
Compare the classical and frequentist interval, where do they differ? where are they are equal? Use the case for example $b=3$.

#### Exercises 3: Hypothesis testing (composite case)

##### Exercise 3a: 
Verify that the $q_0$ distribution is a 'half' $\chi^2$.

**Choose at least one among 3b and 3c.**

##### Exercise 3b:
 Consider the case of a poisson distribution with a unknown mean $\mu$ and the null hypothesis $\mu_0$. Check for which values of $\mu$, $g(t_\mu | \mu)$ follows a $\chi^2(1)$ distribution.

##### Exercise 3c:
Consider the case of an experiment that gets a sample of n-size poisson distributed values, $x$, with a unknown mean $\mu$. Check the values of $n$ for which $g(t_\mu | \mu)$ follows a $\chi^2(1)$ distribution.

**Choose at least one among 3d and 3e**

##### Exercise 3d:
Consider an experiment with a gaussian distribution with mean $\mu$ and sigma 1. Consider $\mu_{true} = \mu_0 = 0$. Obtain the distribution of the upper limits at 90 %CL.

##### Exercise 3e:
Consider an experiment with a $n$ sample of gaussian distributed values with $\mu$ and sigma 1. Consider $\mu_{true} = \mu = 3.5$, verify that $q_\mu$ follows a "half" $\chi^2$ distribution with one dof.
