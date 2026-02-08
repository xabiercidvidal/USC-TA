import matplotlib
import matplotlib.pyplot as plt
plt.style.context('seaborn-colorblind')

import numpy          as np
import scipy.stats    as stats
import scipy.optimize as optimize

import htcore    as htcore
import htplot    as htplot

h0color, h1color, datacolor = 'orange', 'green', 'black'
marker = 'o'

def normal_likelihood(xs, isgaussll = False, ylog = False,mus = np.linspace(-3., 3., 100)):

    ## this comes from the -2 log(e^(x-mu)/(2sigma)), with sigma=1
    def ll(mu, xs):
        dx = (mu-xs)
        return np.sum(dx*dx)

    def gaussll(mu,xs):
        probs = stats.norm.pdf(xs, mu, 1)   
        return -2*np.sum(np.log(probs))
        
    nsize = len(xs)
    
    if isgaussll: 
        lls = np.array([gaussll(mu, xs) for mu in mus])
        lname = '\log {}_{Gauss}\mathcal{L}'
    else:
        lls = np.array([ll(mu, xs) for mu in mus])
        lname = '\log \mathcal{L}'
    
    print('mu mean :', np.mean(xs), ', mu std :', 1./np.sqrt(nsize))

    plt.hist(xs, bins=50, range=(min(mus), max(mus)),
            color = datacolor, histtype = 'step', label = 'data');
    plt.ylabel('events'); plt.xlabel('$x$')
    ax = plt.gca(); axb = ax.twinx()
    axb.plot(mus, lls, alpha=0.5, color='red', lw=2,
             label = r'$-2 \, '+lname+'(x | \mu)$')
    deltaL = np.min(lls) +1
    axb.plot(mus, deltaL*np.ones(len(mus)), ls='--',
             label = r'$\Delta '+lname+'(\mu) = 1$');
    axb.set_ylabel('$-2 \, '+lname+'(x | \mu)$')
    if (ylog): axb.set_yscale('log');
    plt.legend(loc = 1);

    return


def normal_posterior(xs):

    def posterior(x, xs):
        """ the posterior of a gaussian likelihood with known sigma_prior and mu mean,
        and flat prior on mu
        is a gaussian with mean the average of the n-measurements and sigma=sigma_prior/sqrt(n)
        """
        xmean = np.mean(xs)
        msig = np.sqrt(1./(1.*len(xs)))
        return stats.norm.pdf(x, xmean, msig)

    mus = np.linspace(-3., 3., 100)
    pos = np.array([posterior(mu, xs) for mu in mus])

    plt.hist(xs, bins=50, range=(-3., 3.), color= datacolor, histtype='step',
            label='data')
    ax = plt.gca(); axb = ax.twinx();
    axb.plot(mus, pos, color='red', lw=2, label="$p(\mu|x_0)$");
    ax.set_xlabel('$\mu$'); axb.set_ylabel(r"$p(\mu|x_0)$");
    plt.legend()

    return

def dice_posterior(xi, hpriors, faces = [4, 6, 12, 24]):
    ## p(x|mu)
    def pxh(x, xface):
        if (x <= xface): return 1./(1.*xface)
        return 0.

    ## p(x|mu)*p(mu)
    pxhs = np.array([pxh(xi, faces[i])*hpriors[i] for i in range(4)])
    px = np.sum(pxhs)

    ## p(mu|x) = p(x|mu)*p(mu)/px
    hpos = pxhs/px
    print('!')
    #hpos = hpos/np.sum(hpos)
    return hpos


def binomial_poisson(N, p):

    N, p = 100, 0.08
    ns = np.arange(20)
    plt.bar(ns, stats.binom.pmf(ns, N, p), color='blue', alpha=0.5, label='binomial')
    plt.bar(ns, stats.poisson.pmf(ns, N*p), color='red', alpha=0.5, label='poisson')
    plt.xlabel('$x$')
    plt.set_ylabel('$f(x$)', fontsize=16)
    plt.legend(fontsize=14)
    return
