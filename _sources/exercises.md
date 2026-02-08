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
Consider a **hypothetical search for a new particle** at the **LHC**. Assume we are looking for a **new resonance (X) decaying into two photons ($\gamma\gamma$)** in a **100 fb$^{-1}$** dataset at **$(\sqrt{s} = 13$) TeV**. 
**Determine**
- **Signal Yield**: The predicted cross-section for $( pp \to X \to \gamma\gamma $) is **1 fb**, and the detector **acceptance times efficiency** is **50%**. Compute the expected number of signal events.
- **Background Yield**: The main background comes from the **Standard Model diphoton production**, with a **background index of $(5 \times 10^{-3}$) events/(GeV fb$^{-1}$)** at **125 GeV**. Assume an **energy resolution of 1%** at 125 GeV and define the **Region of Interest (RoI) as $(\pm 3\sigma$)**. Compute the expected number of background events.
- **Test Statistics PDFs**: Assume that the **signal invariant mass is normally distributed**. Compute the **expected distributions of the test statistics** under the **signal-plus-background (S+B)** and **background-only (B) hypotheses**.

Analyze how changing the cross-section, background index or energy resolution affect the **signal-to-background ratio** and the **test statistics distributions**.

##### Exercise 2b:
Consider an experiment with several independent channels that expects as background ${\bf b} = (2, 1.5, 1, 0.5)$ and as signal ${\bf s} = (1, 3, 3, 1)$. The measurement is $(2, 1, 1, 0)$. Compute the p-value of $H_1$.



**Choose at least 1 among:**

##### Exercise 2c:
Consider the expected background events and signal events in bins of energy in the RoI of the KamLAND-Zen experiment in Fig 2-b) [PRL-117](https://arxiv.org/abs/1605.02889). 
- Compute now the pdfs of $q$ for only background and 10 times the signal.
- Compute the p-value of $H_0$.

*Guide:* 

From Fig 2-b) Period II we can extract the following number of background, signal and observed events.

*b* = [4.0, 2.0, 1.6, 1.0, 0.8, 0.7, 0.6, 0.5, 0.5, 0.5, 0.6, 0.6, 0.8, 1.1]

*s* = [0.2, 0.4, 0.5, 0.6, 0.5, 0.4, 0.2, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0]

*x* = [4.0, 0.0, 2.0, 4.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 2.0, 2.0, 1.0, 0.0]

##### Exercise 2d:
An experiment expects $(2, 1)$ background events in two bins, and a possible signal $(8, 9)$ on top. 
- If it observes $(9, 9)$, can we claim an observation?
- In case it observes $(1, 1)$, can we reject the signal at 95 % CL?

<!-- #endregion -->

#### Exercises 3: Confidence intervals

##### Exercise 3a: 
Use the classical construction of CI for the case of a gaussian with $\sigma= 1$ and $\beta = 68$ % CL.

<!-- #region -->
**Choose at least 2 among:**

##### Exercise 3b:
Verify that the flip-flop problem has not the proper coverage. For this, set the flip-flop construction and test the coverture for $\mu_{true} = 3$.
Why the case $b=3$ and $x_0 = 0$ has no classical CI at 90% CL?

##### Exercise 3c: 
FC is a frequentist method. Verify now that the FC construction guarantees **coverage** for some examples $b = 3, \mu_{true} = 0.5$

##### Exercise 3d: 
Compare the classical and frequentist intervals, where do they differ? Where are they are equal? Use as example the case $b=3$.

#### Exercises 4: Hypothesis testing (composite case)

##### Exercise 4a: 
Verify that the $q_0$ distribution is a 'half' $\chi^2$.

**Choose at least 1 among:**

##### Exercise 4b:
 Consider the case of a poisson distribution with an unknown mean $\mu$ and the null hypothesis $\mu_0$. Check for which values of $\mu$, $g(t_\mu | \mu)$ follows a $\chi^2(1)$ distribution.

##### Exercise 4c:
Consider an experiment with a gaussian distribution with mean $\mu$ and sigma 1. Consider $\mu_{true} = \mu_0 = 0$. Obtain the distribution of the upper limits at 90 %CL.


#### Exercises 5: Fitting with zfit

##### Exercise 5a: 
You are analyzing data from a high-energy physics experiment (like LHCb). You are studying the rare decay of charmed mesons into an $\eta$ meson and a pion:

1. $D_s^+ \to \eta \pi^+$
2. $D^+ \to \eta \pi^+$

In both cases, the  meson is reconstructed via its dimuon decay mode: : $\eta \to \mu^+ \mu^-$.
Your physics objective is to measure the branching ratio $\mathcal{B}(\eta \to \mu^+\mu^-)$.
This branching ratio is a fundamental constant of nature and must be the **same** regardless of whether the $\eta$ meson came from a  $D_s^+$ or a $D^+$.

You have two [datasets](https://www.dropbox.com/scl/fi/xd5tn9444ggn307d7qzih/zfit_ex_datasets.zip?rlkey=vvfldbo1hjgaiapfhvtupolxr&dl=1): `dataset_Ds.csv` and `dataset_Dp.csv`. 


* **Sample A ($D^+_s$):** Events selected near the $D_s^+$ mass.
* **Sample B ($D^+$):** Events selected near the $D^+$ mass.

Instead of fitting $N_{sig}$ independently and calculating the Branching Ratio (BR) offline, you will perform a Simultaneous Fit to both samples. You will parameterize the signal yield $N_{sig}$ in the fit directly as a function of the physics parameter $\mathcal{B}(\eta \to \mu\mu)$ and a normalization factor $\alpha$ (which includes luminosity, cross-section, and efficiency).

$$\mathcal{B}(\eta \to \mu\mu) = N_{sig} \cdot \alpha \quad \Rightarrow \quad N_{sig}(\mathcal{B}) = \frac{\mathcal{B}}{\alpha}$$

You are given the sensitivity factors $\alpha$ for each channel:

$\alpha_{D^+_s} = 2.5 \times 10^{-5}$

$\alpha_{D^+} = 8.0 \times 10^{-5}$


You are dealing with a 2D problem. The observables are:

1. `mass_D`: The invariant mass of the  $\mu\mu\pi$ system.
2. `mass_eta`: The invariant mass of the  $\mu\mu$ system.

This sample contains three components:

###### Sample 1:  $D_s^+$ Region

This sample contains three components:

1. **Signal ($D^+_s \to \eta \pi$):**
* `mass_D`: Gaussian (Peak at $m_{D^+_s}$).
* `mass_eta`: Gaussian (Peak at $m_\eta$).


2. **Combinatorial Background:**
* `mass_D`: Exponential.
* `mass_eta`: Exponential.


3. **Real $\eta$ Background (Fake $D^+_s$)**:
Contains a real $\eta$, but combined with a random pion:
* `mass_D`: Exponential  (No $D^+_s$ peak).
* `mass_eta`: Gaussian (Real $\eta$ peak).


###### Sample 2:  $D^+$ Region

This sample contains three components:

1. **Signal ($D^+ \to \eta \pi$):**
* `mass_D`: Gaussian (Peak at $m_{D^+}$).
* `mass_eta`: Gaussian (Peak at $m_\eta$).


2. **Combinatorial Background:**
* `mass_D`: Exponential.
* `mass_eta`: Exponential.

3. **Non-Resonant Background (Real $D^+$):**
Contains a real $D^+ \to \mu\mu\pi$ decay, but the muons are not from an $\eta$ meson.
* `mass_D`: Gaussian (Real $D^+$ peak).
* `mass_eta`: Exponential (No $\eta$ peak).


###### Tasks

1. **Model Building:** Construct the 2D PDFs for all 6 components (3 for , 3 for ) using `zfit`. Try to discuss the *meaning* or *origin* of each of the components mentioned above. *Hint:* The Signal and the "Real" background must share the same  mass shape parameters. The centers of the gaussians should be roughly the masses of the relevant particles. You can assume their widths to the be in the range of 5-20 MeV. The background slopes are small and negative, in the $(-10^{-2},-10^{-3})$ range.

2. **Parameterization:** Create a shared parameter `BR_eta_mumu`. Define the signal yields for both samples as composed parameters dependent on this BR.
3. **Simultaneous Fit:** Perform a simultaneous fit to both datasets.
4. **Validation:** Plot the projections of the fit (Mass  and Mass ) for both samples.
5. **Result:** Result: Report the fitted value of $\mathcal{B}(\eta \to \mu\mu)$ and its uncertainty. Does it cover the true value?
6. **Discuss:** How does the precision you achieve in the BR compare to the current world best? How would you improve it? Is there any effect going into the BR uncertainty you are missing? 

**Choose at least 1 among:**

##### Exercise 5b:
Uncertainty Scaling: Check the output of the "extended likelihood" example. In a simple counting experiment, the error on $N$ is $\sqrt{N}$.
1.  Check the error on `n_sig` from the fit output.
2.  Is it larger or smaller than $\sqrt{N_{sig}}$?
3.  **Thought experiment:** Why is it different? (Hint: Does the background shape look like the signal?)

##### Exercise 5c: 
Shared Resolution: Imagine you have a $J/\psi \to \mu\mu$ calibration channel.
1.  Generate a calibration dataset (Pure Gaussian, mean=3100, sigma=25).
2.  Set up a simultaneous fit with your Signal Region.
3.  Share the `sigma` parameter between the Signal Region and the Calibration Channel.
4.  See how this constrains the width of your signal peak.
 
<!-- #endregion -->

```python

```
