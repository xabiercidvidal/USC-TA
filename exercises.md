<!-- #region -->
### Exercises
**Do the following exercises.**

#### Exercises 1: Basic concepts

##### Exercise 1a: 
A neutrino experiment has a problem with the DAQ, and 5% of the running time it does not observe interactions. The neutrinos are produced by a reactor nearby that operates 75% of the time. In this moment, the experiment does not observe neutrinos, what is the probability that the reactor is off?

**Choose at least 1 among:**
##### Exercise 1b:
Check that from a "large" $\nu$ the poisson distribution is equivalent to a gaussian distribution.

##### Exercise 1c:
Generate $m$ datasets, each with $n$ data, $x_i$, normally distributed, compute its distance squared $\chi^2 = \sum_{i=1}^n x^2_i$, what is the distribution of $\chi^2$?

##### Exercise 1d:
Generate $n$ $x_i$-values, each one gaussianly distributed with mean $\mu_i$ and sigma $\sigma_i$, show that the sum $\sum_i x_i$ is gaussian distributed with mean, $\mu = \sum_i \mu_i$, and sigma $\sigma^2 = \sum_i \sigma^2_i$.

**Choose at least 1 among:**
##### Exercise 1e:
Show that the posterior of a normal prior, $\pi(\mu | \mu_0, \sigma_{\mu_0})$,
and a normal likelihood, $p(x |\mu, \sigma)$, for n-measurements, $x$, is a normal distribution with mean, $\mu'$, and sigma, $\sigma_{\mu'}$:

$$
\frac{1}{\sigma^2_{\mu'}} = \frac{n}{\sigma^2} + \frac{1}{\sigma^2_{\mu_0}}, 
\;\;\;
\mu' = \sigma^2_{\mu'} \left( \frac{\mu_0}{\sigma^2_{\mu_0}} + \frac{\sum_i x_i}{\sigma^2} \right)
$$

##### Exercise 1f:
There are several dices in a box, with 4, 6, 12 and 24 sides. We randomly pick one dice and we roll it four times. The outcomes are $\{1,4,5,2\}$. What is the posterior probability that the selected dice has 4, 6, 12 or 24 sides? What is the posterior probability if we roll it twice again and we get now 6 and 1? 
Use the posterior probability formula: 
$$
p(\mu|x) = \frac{p(x|\mu) \, \pi(\mu)}{\sum p(x|\mu) \pi(\mu)}
$$

and bear in mind, for a dice with $\mu$ faces $p(x|\mu)$ will be 0 if $x>\mu$ or $1/\mu$ else.

#### Exercises 2: Hypothesis testing (simple case)

##### Exercise 2a:
Consider an experiment with several independent channels that expects as background ${\bf b} = (2, 1.5, 1, 0.5)$ and as signal ${\bf s} = (1, 3, 3, 1)$. The measurement is $(2, 1, 1, 0)$. Compute the p-value of $H_1$.

##### Exercise 2b: 
Consider a **hypothetical search for a new particle** at the **LHC**. Assume we are looking for a **new resonance (X) decaying into two photons ($\gamma\gamma$)** in a **100 fb$^{-1}$** dataset at **$(\sqrt{s} = 13$) TeV**. 
**Determine**
- **Signal Yield**: The predicted cross-section for $( pp \to X \to \gamma\gamma $) is **1 fb**, and the detector **acceptance times efficiency** is **50%**. Compute the expected number of signal events.
- **Background Yield**: The main background comes from the **Standard Model diphoton production**, with a **background index of $(5 \times 10^{-3}$) events/(GeV fb$^{-1}$)** at **125 GeV**. Assume an **energy resolution of 1%** at 125 GeV and define the **Region of Interest (RoI) as $(\pm 3\sigma$)**. Compute the expected number of background events.
- **Test Statistics PDFs**: Assume that the **signal is normally distributed**. Compute the **expected distributions of the test statistics** under the **signal-plus-background (S+B)** and **background-only (B) hypotheses**.

Analyze how changing the cross-section, background index or energy resolution affect the **signal-to-background ratio** and the **test statistics distributions**.


**Choose at least 1 among:**

##### Exercise 2c:
Consider the expected background events and signal events in bins of energy in the RoI of the KamLAND-Zen experiment in Fig 2-b) [PRL-117](https://arxiv.org/abs/1605.02889). 
- Compute now the pdfs of $q$ for only background and 10 times the signal.
- Compute the p-value of $H_0$.

##### Exercise 2d:
An experiment expects $(2, 1)$ background events in two bins, and a possible signal $(8, 9)$ on top. 
- If it observes $(9, 9)$, can we claim an observation?
- In case it observes $(1, 1)$, can we reject the signal at 95 % CL?

<!-- #endregion -->

#### Exercises 3: Confidence intervals

##### Exercise 3a: 
Use the classical construction of CI for the case of a gaussian with $\sigma= 1$ and $\beta = 68$ % CL.


**Choose at least 2 among:**

##### Exercise 3b:
Verify that the flip-flop problem has not the proper coverage.

##### Exercise 3c: 
FC is a frequentist method. Verify now that the FC contruction guarantees **coverage** for some examples $b = 3, \mu_{true} = 0.5$

##### Exercise 3d: 
Compare the classical and frequentist interval, where do they differ? where are they are equal? Use the case for example $b=3$.

#### Exercises 4: Hypothesis testing (composite case)

##### Exercise 4a: 
Verify that the $q_0$ distribution is a 'half' $\chi^2$.

**Choose at least 1 among:**

##### Exercise 4b:
 Consider the case of a poisson distribution with a unknown mean $\mu$ and the null hypothesis $\mu_0$. Check for which values of $\mu$, $g(t_\mu | \mu)$ follows a $\chi^2(1)$ distribution.

##### Exercise 4c:
Consider the case of an experiment that gets a sample of n-size poisson distributed values, $x$, with a unknown mean $\mu$. Check the values of $n$ for which $g(t_\mu | \mu)$ follows a $\chi^2(1)$ distribution.

**Choose at least 1 among:**

##### Exercise 4d:
Consider an experiment with a gaussian distribution with mean $\mu$ and sigma 1. Consider $\mu_{true} = \mu_0 = 0$. Obtain the distribution of the upper limits at 90 %CL.

##### Exercise 4e:
Consider an experiment with a $n$ sample of gaussian distributed values with $\mu$ and sigma 1. Consider $\mu_{true} = \mu = 3.5$, verify that $q_\mu$ follows a "half" $\chi^2$ distribution with one dof.
