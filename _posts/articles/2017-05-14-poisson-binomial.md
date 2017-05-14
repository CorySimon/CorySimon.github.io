---
layout: post
title: Relating the binomial and Poisson distributions
excerpt: "The binomial and Poisson distributions are equivalent under a limit. This is a helpful interpretation."
comments: true
categories: articles
share: true
tags: [Math, Statistics]
---

The Poisson and binomial distributions become equivalent under a limit. Understanding this lends a helpful interpretation of the Poisson distribution. In this post, we will build our way up to the Poisson distribution under the context of owning of a coffee shop in Seattle.

# The Bernoulli distribution

A given pedestrian is approaching our coffee shop. :runner:

Let $$X$$ be the binary random variable that indicates whether that person
<br/>(i) comes in to buy coffee ($$X=$$:coffee:) or
<br/>(ii) passes by and continues walking in the rain ($$X=$$:umbrella:). [This is Seattle!]

The Bernoulli distribution specifies the probabilities $$Pr(\cdot)$$ of outcome (i) as $$p$$ and outcome (ii) as $$1-p$$:

$$Pr(X=$$:coffee:$$) = p$$

$$Pr(X=$$:umbrella:$$) = 1-p.$$

# The binomial distribution

Consider today when many pedestrians are walking by our coffee shop. Let us model the outcome of whether or not each pedestrian stops by our coffee shop with the Bernoulli distribution above (same $$p$$ for each pedestrian). Assume each pedestrian behaves independently of what the others do. 

Given $$n$$ :runner:'s walk by our coffee shop today, what is the probability that $$k$$ of them stop in to buy a coffee :coffee:? That's the binomial distribution.

The probability of observing a *particular* sequence of $$k$$ coffee buyers and $$n-k$$ passerbys is $$p^k(1-p)^{n-k}$$. For example, for $$n=3$$ and $$k=1$$, the probability of the sequence :umbrella: :umbrella: :coffee: is $$(1-p)^2p$$.

For a given $$n$$ and $$k$$, there are $$\binom{n}{k}$$ different ways to arrange $$k$$ :coffee:'s and $$n-k$$ :umbrella:'s into a sequence. See previous post [here](http://corysimon.github.io/articles/counting/). For $$n=3$$ and $$k=1$$, there are $$\binom{3}{1}=3$$ ways: (1) :umbrella: :umbrella: :coffee: (2) :umbrella: :coffee: :umbrella: and (3) :coffee: :umbrella: :umbrella:.

Accounting for these different arrangements, the binomial distribution is:

$$Pr(k$$ :coffee:'s, $$n-k$$ :umbrella:'s$$) = \binom{n}{k}p^k(1-p)^{n-k}.$$

You can work out the expected value of the Bernoulli distribution to be $$np$$. This is intuitive: in the long run, we expect a fraction $$p$$ of the $$n$$ pedestrians to stop in and buy a coffee.

# The Poisson distribution

Now, imagine instead that we're interested in modeling the random variable $$C$$ that is the count of pedestrians :runner: that walk by our coffee shop in a given hour. Suppose that on average, we see $$E(C)= 6$$ people walk by our coffee shop each hour.

Our first modeling approach might be to break up the hour into intervals of 5 minutes. There are 12 such 5 minute time intervals in an hour. Then, for each interval of 5 minutes, we can model the binary outcome of a pedestrian walking by (or not) as a Bernoulli random variable with probability $$p$$.

The count of pedestrians walking by in an hour would then follow a binomial distribution with $$n=12$$ Bernoulli trials and $$p=1/2$$, since we have on average $$E(C) = np=6$$ pedestrians each hour.

While breaking time into discrete, consecutive intervals yields the correct average behavior, it is an inadequate way of modeling the pedestrian count since it does not allow for the possibility of:
<br/>(i) more than one pedestrian walking by in a given 5 minute interval or 
<br/>(ii) greater than 12 pedestrians walking by in the hour.

We can mitigate each of the two issues above by breaking time into even smaller intervals. Breaking the hour into $$n=60$$ intervals, where each minute is a Bernoulli trial, we would set $$p=1/10$$ to maintain that $$E(C)= np=6$$. Since $$p$$ is smaller than when we had $$n=12$$ intervals, we mitigate the possibility of (i) and account for up to 60 pedestrians walking by our coffee shop to address (ii).

We can make the time intervals as small as we want under this binomial distribution framework, as long as we also make $$p$$ small enough such that $$np=E(C)=6$$. In the limit of infinitely small time intervals, when $$n \rightarrow \infty$$, holding the average $$\lambda:=np$$ fixed, we recover the Poisson distribution:

$$Pr(C=c)=e^{-\lambda}\frac{\lambda^c}{c!}$$ for $$c=0,1,2,3,...$$

So, the Poisson distribution is a stochastic model of event counts in a given time interval. It partitions the time interval into infinitely small subintervals and models the binary outcome of the event of interest occurring in each interval as an independent, Bernoulli trial. To maintain an expected value of event counts of $$\lambda$$, we simultaneously need $$p\rightarrow0$$ for each Bernoulli trail in the infinitely small subintervals. Below, we formalize this.

This interpretation of the Poisson process as an infinite series of identical, independent Bernoulli trials is helpful in understanding why the Poisson process is memoryless: the previous events do not affect the outcome of the future. See my previous post [here](http://corysimon.github.io/articles/the-poisson-process/).

# The math of the Poisson limit theorem

For a random variable $$X$$ that follows the binomial distribution with $$n$$ trials:

$$Pr(X=k) = \binom{n}{k}p^k(1-p)^{n-k}.$$

Our goal is to show that we recover the Poisson distribution with average $$\lambda:= np$$ when we take the limit $$n\rightarrow \infty$$ while holding $$np$$ fixed. To achieve this, we specify that *both* $$n\rightarrow \infty$$ and $$p\rightarrow 0$$ at rates such that the average $$np$$ remains fixed. That is, we will show that:

$$\lim_{n\rightarrow\infty | np \text{ fixed}} \binom{n}{k}p^k(1-p)^{n-k} = e^{-\lambda}\frac{\lambda^k}{k!}.$$

First, write the limit in terms of $$\lambda:=np$$ and write the binomial term as factorials:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \frac{n!}{(n-k)!k!} \left( \frac{\lambda}{n} \right)^k \left( 1-\frac{\lambda}{n} \right)^{n-k}.$$

Then, pull out the $$n^k$$ term:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \frac{n!}{(n-k)! n^k} \frac{1}{k!}\left( \lambda \right)^k \left( 1-\frac{\lambda}{n} \right)^{n-k},$$

and split up the $$(\cdot)^{n-k}$$ term into two products:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \frac{\lambda^k}{k!} \frac{n!}{(n-k)! n^k} \left( 1-\frac{\lambda}{n} \right)^{n}\left( 1-\frac{\lambda}{n} \right)^{-k}.$$

It suffices to show that:

$$\lim_{n \rightarrow \infty | \lambda \text{ fixed}} \frac{n!}{(n-k)! n^k} \left( 1-\frac{\lambda}{n} \right)^{n}\left( 1-\frac{\lambda}{n} \right)^{-k}=e^{-\lambda}.$$

since then we recover the Poisson distribution.

First, focus on the limit:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \frac{n!}{(n-k)! n^k}$$

The $$(n-k)!$$ term in the denominator cancels out terms in the product $$n!$$ in the numerator.

$$\frac{n!}{(n-k)! n^k} = \frac{n(n-1)(n-2)\cdots(n-k-1)}{n^k}.$$

The numerator is thus a $$k$$th order polynomial in $$n$$. As $$n\rightarrow\infty$$, the dominant term in the numerator is $$n^k$$; the sizes of the lower order terms pale in comparison. So, as $$n\rightarrow \infty$$, this term behaves like $$n^k / n^k$$ and consequently:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \frac{n!}{(n-k)! n^k} = 1$$

Next, focus on the limit:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \left( 1-\frac{\lambda}{n} \right)^{-k} = 1/\left( 1-\frac{\lambda}{n} \right)^{k}$$

As $$n\rightarrow\infty$$, the $$\lambda / n \rightarrow 0$$ since $$\lambda$$ is held fixed. The inside of the parentheses then approaches 1. Multiplying 1 by itself $$k$$ times is 1 ($$k$$ is under no limit here). Consequently:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \left( 1-\frac{\lambda}{n} \right)^{-k} = 1/\left( 1-\frac{\lambda}{n} \right)^{k}=1$$

Finally, focus on the limit:

$$\lim_{n\rightarrow\infty | \lambda \text{ fixed}} \left( 1-\frac{\lambda}{n} \right)^{n}.$$

This one is famous. As directly above, the inside of the parenthesis goes to 1, but the numerator also goes to infinity. So we are multiplying a number a little more than 1 an infinite number of times. One student in the room might say the limit is equal to 1 as directly above. Another might say the limit is $$\infty$$ because we are multiplying a number [slightly] greater than one by itself many times. Both students are wrong-- this limit amazingly goes to the mathematical constant $$e^{-\lambda}$$, where $$e \approx 2.71828$$. This is in fact a way to define the exponential constant $$e$$:

$$e:=\lim_{n\rightarrow\infty} \left(1+\frac{1}{n}\right)^n.$$

See [Wikipedia](https://en.wikipedia.org/wiki/E_(mathematical_constant)). You might recognize this as continuously compounding interest.

As the limit of a product of functions is the product of the limits when the limits are finite, we have proven that:

$$\lim_{n \rightarrow \infty | \lambda \text{ fixed}} \frac{n!}{(n-k)! n^k} \left( 1-\frac{\lambda}{n} \right)^{n}\left( 1-\frac{\lambda}{n} \right)^{-k}=e^{-\lambda},$$

and shown the connection between the Poisson and binomial distributions.
